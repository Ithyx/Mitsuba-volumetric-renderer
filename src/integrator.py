from typing import Optional

import drjit as dr
import mitsuba as mi

class GodraysIntegrator(mi.SamplingIntegrator):
    def __init__(self, props: mi.Properties) -> None:
        super().__init__(props)

    def sample(self, scene: mi.Scene, sampler: mi.Sampler, ray: mi.RayDifferential3f, medium: Optional[mi.Medium] = None, active: bool = True ) -> tuple[mi.Color3f, bool, list[float]]:
        color = dr.zeros(mi.Color3f)

        # Intersection initiale
        its: mi.SurfaceInteraction3f = scene.ray_intersect(ray)

        if (dr.any(its.is_valid())):
            # Intersection de sortie ou contre une surface dans le volume
            ray2 = its.spawn_ray(ray.d)
            its2 = scene.ray_intersect(ray2)

            color[its2.is_valid()] = mi.Color3f(its2.t/4, 0.0, 0.0)

        return (color, True, [])
