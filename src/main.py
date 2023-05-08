import config
import matplotlib.pyplot as plt

# autopep8: off
import mitsuba as mi
print(f"Using variant {config.mitsuba_variant}")
mi.set_variant(config.mitsuba_variant)

from integrator import GodraysIntegrator
# autopep8: on

def main():
    mi.register_integrator("godrays", lambda props: GodraysIntegrator(props))

    scene = mi.load_file("scenes/modified/simple_light.xml")
    image = mi.render(scene, spp=128)

    plt.axis('off')
    plt.imshow(image ** (1.0 / 2.2))
    plt.show()


if __name__ == "__main__":
    main()
