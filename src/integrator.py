from typing import cast, Optional

import drjit as dr
import mitsuba as mi

class GodraysIntegrator(mi.SamplingIntegrator):
    def __init__(self, props: mi.Properties) -> None:
        super().__init__(props)
        print("Integator parameters:")

        self.light_data = cast(mi.Emitter, props.get('input_light'))
        self.input_light_pos = cast(mi.Point3f, self.light_data.bbox().center())
        self.step_count = cast(int, props.get('step_count', 20))
        self.density = cast(float, props.get('density', 1.0))

        print(f"\tInput light position: {self.input_light_pos}")
        print(f"\tStep count: {self.step_count}")
        print(f"\tMedium density: {self.density}")

    def sample(self, scene: mi.Scene, sampler: mi.Sampler, ray: mi.RayDifferential3f, medium: Optional[mi.Medium] = None, active: bool = True ) -> tuple[mi.Color3f, bool, list[float]]:
        print("==========================")
        print("      Sampling begin      ")
        print("                          ")
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
            for step_it in range(0, self.step_count + 1):
                print(f"Iteration {step_it + 1}, t = {step_distance * step_it} (max_t = {distance})")
                # Génération d'un rayon vers la lumière sélectionnée à partir du step
                scatter_origin = ray2(step_distance * step_it)
                scatter_dir = self.input_light_pos - scatter_origin # type: ignore (Is this really doing what I think it is?)
                scatter_ray = mi.Ray3f(scatter_origin, scatter_dir)
                scatter_its = cast(mi.SurfaceInteraction3f, scene.ray_intersect(scatter_ray))

                print(f"\tScatter ray origin: {scatter_origin}")
                print(f"\tScatter ray direction: {scatter_dir}")
                print(f"\tScatter ray distance to next hit: {scatter_its.t}")

                # TODO: check for occlusion
                # TODO: make sure this works for light inside the volume

                # Calcul de la transmittance à partir de la densité (homogène)
                # https://www.pbr-book.org/3ed-2018/Light_Transport_II_Volume_Rendering/Sampling_Volume_Scattering#HomogeneousMedium
                scatter_transmittance = dr.exp(-(self.density * scatter_its.t))
                step_transmittance = dr.exp(-(self.density * step_distance * step_it))
                
                light_accumulator += scatter_transmittance * step_transmittance

            color[its.is_valid()] = light_accumulator

        return (color, True, [])
