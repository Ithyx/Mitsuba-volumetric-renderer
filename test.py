import mitsuba as mi

mi.set_variant('cuda_ad_rgb')

img = mi.render(mi.load_file("scenes/base/cbox.xml"), spp=256)

mi.Bitmap(img).write('out.exr')
