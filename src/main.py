import mitsuba as mi

mi.set_variant("llvm_ad_rgb")
# mi.set_variant("scalar_rgb")

import matplotlib.pyplot as plt

from integrator import GodraysIntegrator


def main():
    mi.register_integrator("godrays", lambda props: GodraysIntegrator(props))

    scene = mi.load_file("scenes/modified/simple_light.xml")
    image = mi.render(scene, spp=128) # type: ignore (Yes is does work what are you doing pylance)

    plt.axis('off')
    plt.imshow(image ** (1.0 / 2.2)) # type: ignore (This also work I hate python)
    plt.show()


if __name__ == "__main__":
    main()
