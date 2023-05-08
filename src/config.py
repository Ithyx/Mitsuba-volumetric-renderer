debug = True
mitsuba_variant = "scalar_rgb" if debug else "llvm_ad_rgb"

def cprint(string: str) -> None:
    if debug:
        print(string)

