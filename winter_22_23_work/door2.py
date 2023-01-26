import numpy as np
import matplotlib.pyplot as plt
import math
from shapely import transform, intersection
from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry.polygon import Polygon
import vnoise
noise = vnoise.Noise()

LINE_COLOR = "#000000"
IMG_SIZE = (1400, 1060)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]
LINE_WIDTH = 2
offset_x = 600
offset_y = Y_BOUND/2+10
scale = 1

base = 1.031
n_doors = 20
hall_vect = np.linspace(1, 100**base, n_doors)
def log_np(v, base):
    return(np.log(v)/np.log(base))
logs = log_np(hall_vect, base)
radius = 200
points_in_semi_circle = 100

hallway_steepness = .8
door_bottom_x = -300


def close_path(f):
    f.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(f, x, y):
    f.write('<path d="M {},{}'.format(x, y))

def add_point(f, x, y):
    f.write(' L {},{}'.format(x, y))

def arch(radius, hallway_steepness, door_bottom_x, offset_y = offset_y, i = 1, y_drift_rate = 0, connect_bottom = False):
    theta = np.linspace(0, np.pi, points_in_semi_circle)

    semi_x = np.sin(theta)*(radius - i*1.2) - i + 100 - .5*i
    semi_y = np.cos(theta)*(radius - i*1.2) - i*y_drift_rate

    # add points for the bottom of the door
    semi_x[0] = i*hallway_steepness + door_bottom_x
    semi_x[-1] = i*hallway_steepness + door_bottom_x

    zipped_coords = zip(semi_x + offset_x, semi_y + offset_y)
    coords = [(x,y) for x,y in zipped_coords]
    if connect_bottom:
        coords.append(coords[0])
    return(LineString(coords))

def translate(v, x = 5, y = 0):
    v[:,1] = v[:,1] + x
    return(v)

def scale(v, s = .5):
    return(.5*v)

def door(offset_y, y_drift_rate = 1):
    paths = []
    for i in logs:
        paths.append(arch(radius, hallway_steepness, door_bottom_x, offset_y, i, y_drift_rate))

    # last doors
    last_door = Polygon(paths[-1])

    # door bottoms
    floor_coords = [paths[0].coords[0], paths[0].coords[-1], paths[-1].coords[-1], paths[-1].coords[0], paths[0].coords[0]]
    paths.append(LineString([(c[0],c[1]) for c in floor_coords]))

    for d in np.arange(0,20,5):
        shifted_door = transform(last_door, translate)
        shifted_door = intersection(shifted_door, last_door)
        #shifted_door = [p for p in intersection(shifted_door, last_door).coords if not last_door.contains(p)]
        paths.append(shifted_door.boundary)
    # hall_turn_increment = 4
    # for j in range(10):
    #     i = logs[-1]
    #     # Generate points along a semicircle
    #     theta = np.linspace(0, np.pi, points_in_semi_circle)
    #     xs = scale*(np.sin(theta)*(radius - i*1.2) - i + 100 - .5*i) + offset_x
    #     ys = scale*(np.cos(theta)*(radius - i*1.2) - i + hall_turn_increment*j) + offset_y
    #     xs[-1] = i*hallway_steepness + door_bottom_x + offset_x + 1
    #     path = LineString([(x,y) for x,y in zip(xs,ys)]) #if last_door.contains(Point(x,y))])
    #     if len(path.coords) > 0:
    #         paths.append(path)
    return(paths)


paths = []
paths = paths + door(Y_BOUND/2) + door(Y_BOUND*3/2, -1) + door(Y_BOUND, 0)
paths.append(arch(800, hallway_steepness, door_bottom_x, offset_y = 1050, connect_bottom = True))

f = open("door2.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

last_door_idx = len(logs)-1

start_path(f, 0, 0)
add_point(f, X_BOUND-1, 0)
add_point(f, X_BOUND-1, Y_BOUND-1)
add_point(f, 0, Y_BOUND-1)
close_path(f)

# write paths to svg file
for path in paths:
    path = transform(path, scale)
    coords = list(path.coords)
    start_path(f, coords[0][0], coords[0][1])
    for c in coords[1:]:
        add_point(f, c[0], c[1])
    close_path(f)

f.write('</svg>\n')

# Close the file
f.close()
