from typing import Tuple
import drjit as dr
import mitsuba as mi

from phase_function import SunBeamPhaseFunction


class SunBeamPrimitive(mi.Medium):
    def __init__(self: mi.Medium, props: mi.Properties) -> None:
        mi.Medium.__init__(props)

    def eval_tr_and_pdf(self: mi.Medium, mi, si, active: bool) -> Tuple[mi.Color3f, mi.Color3f]:
        # TODO
        return ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

    def is_homogeneous(self: mi.Medium) -> bool:
        return False

    def phase_function(self: mi.Medium) -> SunBeamPhaseFunction:
        return SunBeamPhaseFunction()

    def sample_interaction(self: mi.Medium, ray: mi.Ray3f, sample: float, channel: int, active: bool) -> mi.MediumInteraction3f:
        # TODO
        return super().sample_interaction(ray, sample, channel, active)
