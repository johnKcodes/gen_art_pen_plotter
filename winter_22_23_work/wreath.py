# create a script that will create an svg file with a circle using the shapely library

import shapely.geometry as sg
import shapely.affinity as sa
import svgwrite

axi_error_scale = 305/246
IMG_SIZE = (1152*axi_error_scale, 864*axi_error_scale)
f = open("cp_test.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))
# create a circle

circle = sg.Point(0, 0).buffer(1)

# create a shape that is the intersection of two circles
circle1 = sg.Point(400, 400).buffer(200)
circle2 = sg.Point(600, 500).buffer(200)
shape = circle1.intersection(circle2)

dwg = svgwrite.Drawing('test.svg', profile='tiny')

# now repeat this process until it reaches 360 degrees
for i in range(0,360,10):
    shape_i = sa.rotate(shape, i)
    new_shape = shape_i.difference(sa.rotate(shape, i-10))

    f.write(new_shape.svg(fill_color = 'none'))

f.write('</svg>\n')
f.close()

