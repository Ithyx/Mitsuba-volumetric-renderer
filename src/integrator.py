from typing import Optional

import mitsuba as mi
import drjit as dr

class GodraysIntegrator(mi.MonteCarloIntegrator):
    def __init__(self, props: mi.Properties):
        mi.MonteCarloIntegrator.__init__(self, props)

    def sample(self, scene: mi.Scene, sampler: mi.Sampler, ray: mi.RayDifferential3f, medium: Optional[mi.Medium] = None, active: bool = True ) -> tuple[mi.Color3f, bool, list[float]]:

        return (color, escaped, [])
