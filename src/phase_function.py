import drjit as dr
import mitsuba as mi


class SunBeamPhaseFunction(mi.PhaseFunction):
    # TODO
    def __init__(self: mi.PhaseFunction) -> None:
        props = mi.Properties()
        mi.PhaseFunction.__init__(self, props)
