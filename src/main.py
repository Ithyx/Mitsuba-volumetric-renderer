# autopep8: off
import mitsuba as mi
mi.set_variant("llvm_ad_rgb")

from primitive import SunBeamPrimitive

# autopep8: on


def main():
    mi.register_medium("sunbeam", lambda props: SunBeamPrimitive(props))

    scene = mi.load_file("scenes/modified/cbox.xml")
    image = mi.render(scene, spp=256)

    mi.util.write_bitmap("out.exr", image)


if __name__ == "__main__":
    main()
