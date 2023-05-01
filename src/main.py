# autopep8: off
import mitsuba as mi
mi.set_variant("llvm_ad_rgb")

from integrator import GodraysIntegrator

# autopep8: on


def main():
    mi.register_integrator("godrays", lambda props: GodraysIntegrator(props))

    scene = mi.load_file("scenes/modified/cbox.xml")
    image = mi.render(scene, spp=256)

    mi.util.write_bitmap("out.exr", image)


if __name__ == "__main__":
    main()
