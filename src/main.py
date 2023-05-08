# autopep8: off
import mitsuba as mi
mi.set_variant("llvm_ad_rgb")
# mi.set_variant("scalar_rgb")

from integrator import GodraysIntegrator

import matplotlib.pyplot as plt

# autopep8: on


def main():
    mi.register_integrator("godrays", lambda props: GodraysIntegrator(props))

    scene = mi.load_file("scenes/modified/simple_light.xml")
    image = mi.render(scene, spp=128)

    plt.axis('off')
    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    main()
