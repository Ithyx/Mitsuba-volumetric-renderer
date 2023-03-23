import mitsuba as mi

from primitive import SunBeamPrimitive


def main():
    mi.set_variant("llvm_ad_rgb")
    mi.register_medium("sunbeam", lambda props: SunBeamPrimitive(props))

    scene = mi.load_file("scenes/modified/cbox.xml")
    image = mi.render(scene, spp=256)

    mi.util.write_bitmap("out.exr", image)


if __name__ == "__main__":
    main()
