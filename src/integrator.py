from typing import cast, Optional
from math import exp

import drjit as dr
import mitsuba as mi

class GodraysIntegrator(mi.SamplingIntegrator):
    def __init__(self, props: mi.Properties) -> None:
        super().__init__(props)

        light_data = cast(mi.Emitter, props.get('input_light'))

        self.input_light_pos = cast(mi.Point3f, light_data.bbox().center())
        self.step_count = cast(int, props.get('step_count', 20))
        self.density = cast(float, props.get('density', 0.7))

    def sample(self, scene: mi.Scene, sampler: mi.Sampler, ray: mi.RayDifferential3f, medium: Optional[mi.Medium] = None, active: bool = True ) -> tuple[mi.Color3f, bool, list[float]]:
        color = dr.zeros(mi.Color3f, shape=1)

        # Intersection initiale
        its = cast(mi.SurfaceInteraction3f, scene.ray_intersect(ray))

        if (dr.any(its.is_valid())):
            # Intersection de sortie ou contre une surface dans le volume
            ray2 = its.spawn_ray(ray.d)
            its2 = cast(mi.SurfaceInteraction3f, scene.ray_intersect(ray2))

            # Distance entre le point d'entrée dans la shape et le point de sortie/d'intersection
            distance = its2.t
            step_distance = distance / self.step_count

            for step in dr.linspace(dtype=dr.llvm.ad.ArrayXf, start=step_distance, stop=distance, num=self.step_count, endpoint=False):
                # Génération d'un rayon vers la lumière sélectionnée à partir du step
                scatter_origin = ray2(step)
                scatter_dir = self.input_light_pos - scatter_origin # type: ignore (Is this really doing what I think it is?)
                scatter_ray = mi.Ray3f(scatter_origin, scatter_dir)
                scatter_its = cast(mi.SurfaceInteraction3f, scene.ray_intersect(scatter_ray))

                # TODO: check for occlusion
                # TODO: make sure thos works for light inside the volume

                # Calcul de la transmittance à partir de la densité (homogène)
                # https://www.pbr-book.org/3ed-2018/Light_Transport_II_Volume_Rendering/Sampling_Volume_Scattering#HomogeneousMedium
                transmittance = exp(-(self.density * scatter_its.t))

        return (color, True, [])
