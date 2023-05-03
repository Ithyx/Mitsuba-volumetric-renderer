from typing import Optional

import drjit as dr
import mitsuba as mi

class GodraysIntegrator(mi.SamplingIntegrator):
    def __init__(self, props: mi.Properties) -> None:
        super().__init__(props)

        self.input_light = props.get('input_light')
        self.step_count = props.get('step_count')
        print(f"input light: {self.input_light}")
        print(f"step count: {self.step_count}")

    def sample(self, scene: mi.Scene, sampler: mi.Sampler, ray: mi.RayDifferential3f, medium: Optional[mi.Medium] = None, active: bool = True ) -> tuple[mi.Color3f, bool, list[float]]:
        color = dr.zeros(mi.Color3f, shape=1)

        # Intersection initiale
        its = mi.SurfaceInteraction3f(scene.ray_intersect(ray))

        if (dr.any(its.is_valid())):
            # Intersection de sortie ou contre une surface dans le volume
            ray2 = its.spawn_ray(ray.d)
            its2 = mi.SurfaceInteraction3f(scene.ray_intersect(ray2))

            # Distance entre le point d'entrée dans la shape et le point de sortie/d'intersection
            distance = its2.t



        print(type(color))
        return (color, True, [])
