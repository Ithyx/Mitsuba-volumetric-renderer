import drjit as dr
import mitsuba as mi


class SunBeamPhaseFunction(mi.PhaseFunction):
    # TODO
    def __init__(self: mi.PhaseFunction, props: mi.Properties) -> None:
        mi.PhaseFunction.__init__(props)
