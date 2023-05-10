from typing import cast, Optional

import mitsuba as mi

import drjit as dr

from config import cprint


class GodraysIntegrator(mi.SamplingIntegrator):
    def __init__(self, props: mi.Properties) -> None:
        super().__init__(props)
        cprint("Integator parameters:")

        self.light_data = cast(mi.Emitter, props.get('input_light'))
        self.input_light_pos = cast(mi.Point3f, self.light_data.bbox().center())
        self.step_count = cast(int, props.get('step_count', 20))
        self.density = cast(float, props.get('density', 1.0))

        cprint(f"\tInput light position: {self.input_light_pos}")
        cprint(f"\tStep count: {self.step_count}")
        cprint(f"\tMedium density: {self.density}")

    def sample(self, scene: mi.Scene, sampler: mi.Sampler, ray: mi.RayDifferential3f, medium: Optional[mi.Medium] = None, active: bool = True ) -> tuple[mi.Color3f, bool, list[float]]:
        cprint("==========================")
        cprint("      Sampling begin      ")
        cprint("                          ")
        color = dr.zeros(mi.Color3f)

        # Intersection initiale
        its = cast(mi.SurfaceInteraction3f, scene.ray_intersect(ray))

        if (dr.any(its.is_valid())):
            # Intersection de sortie ou contre une surface dans le volume
            ray2 = its.spawn_ray(ray.d)
            its2 = cast(mi.SurfaceInteraction3f, scene.ray_intersect(ray2))

            # Distance entre le point d'entrée dans la shape et le point de sortie/d'intersection
            distance = its2.t
            step_distance = distance / self.step_count

            light_accumulator = dr.zeros(mi.Color3f)
            transmission = 1.0
            for step_it in range(0, self.step_count + 1):
                cprint(f"Iteration {step_it + 1}, t = {step_distance * step_it} (max_t = {distance})")
                # Génération d'un rayon vers la lumière sélectionnée à partir du step
                scatter_origin = ray2(step_distance * step_it)
                scatter_dir = self.input_light_pos - scatter_origin # type: ignore (Is this really doing what I think it is?)
                scatter_ray = mi.Ray3f(scatter_origin, scatter_dir)
                scatter_its = cast(mi.SurfaceInteraction3f, scene.ray_intersect(scatter_ray))

                # cprint(f"\tScatter ray origin: {scatter_origin}")
                # cprint(f"\tScatter ray direction: {scatter_dir}")
                # cprint(f"\tScatter ray distance to next hit: {scatter_its.t}")

                # TODO: check for occlusion
                # TODO: make sure this works for light inside the volume

                # Calcul de la transmittance à partir de la densité (homogène)
                # https://www.pbr-book.org/3ed-2018/Light_Transport_II_Volume_Rendering/Sampling_Volume_Scattering#HomogeneousMedium
                scatter_transmittance = dr.exp(-(self.density * scatter_its.t)) * step_distance

                cprint(f"scatter transmittance: {scatter_transmittance}")
                
                # TODO: composite samples
                # forward ray marching (as described in (https://www.scratchapixel.com/lessons/3d-basic-rendering/volume-rendering-for-developers/ray-marching-algorithm.html)
                sample_transmission = dr.exp(-(step_distance * self.density))
                transmission *= sample_transmission
                light_accumulator += scatter_transmittance * transmission

            color[its.is_valid()] = light_accumulator

        return (color, True, [])
