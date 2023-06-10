# write a script to create a circle with the shapely library and write it to an svg file
# import the shapely library
from shapely.geometry import Point, Polygon
# import the svgwrite library
import svgwrite
    
# create a circle with a radius of 100
circle = Point(0, 0).buffer(100)
# create a polygon from the circle
poly = Polygon(circle.exterior.coords)
# create a list of the coordinates of the polygon
coords = list(poly.exterior.coords)
# create a list of the x coordinates of the polygon
x = [i[0] for i in coords]
# create a list of the y coordinates of the polygon
y = [i[1] for i in coords]
# create a list of the x and y coordinates of the polygon
xy = [i for i in zip(x, y)]
# now write the coordinates to an svg file
dwg = svgwrite.Drawing('circle.svg', profile='tiny')
dwg.add(dwg.polygon(xy))
dwg.save()

