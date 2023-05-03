# autopep8: off
import mitsuba as mi
mi.set_variant("llvm_ad_rgb")

from integrator import GodraysIntegrator

import matplotlib.pyplot as plt

# autopep8: on


def main():
    mi.register_integrator("godrays", lambda props: GodraysIntegrator(props))
    params = {}
    params["integrator"] = "godrays"

    scene = mi.load_file("scenes/modified/simple_light.xml", **params)
    image = mi.render(scene, spp=128)

    plt.axis('off')
    plt.imshow(image ** (1.0 / 2.2))
    plt.show()


if __name__ == "__main__":
    main()
