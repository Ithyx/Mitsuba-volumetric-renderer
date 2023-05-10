import mitsuba as mi

mi.set_variant("llvm_ad_rgb")
# mi.set_variant("scalar_rgb")

import matplotlib.pyplot as plt

from integrator import GodraysIntegrator


def main():
    mi.register_integrator("godrays", lambda props: GodraysIntegrator(props))

    scene = mi.load_file("scenes/modified/simple_light.xml")
    image = mi.render(scene, spp=128)

    plt.axis('off')
    plt.imshow(image ** (1.0 / 2.2))
    plt.show()


if __name__ == "__main__":
    main()
