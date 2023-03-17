import mitsuba as mi

mi.set_variant('scalar_rgb')

img = mi.render(mi.load_file("scenes/volumetric_caustic.xml"), spp=256)

mi.Bitmap(img).write('out.exr')
