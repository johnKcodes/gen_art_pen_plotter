import numpy as np
import matplotlib.pyplot as plt
import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import vnoise
noise = vnoise.Noise()

LINE_COLOR = "#000000"
IMG_SIZE = (1400, 1060)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]
LINE_WIDTH = 2
offset_x = 600
offset_y = Y_BOUND/2+10x
scale = 1

def close_path(f):
    f.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(f, x, y):
    f.write('<path d="M {},{}'.format(x, y))

def add_point(f, x, y):
    f.write(' L {},{}'.format(x, y))

base = 1.031
n_doors = 50
hall_vect = np.linspace(1, 100**base, n_doors)
def log_np(v, base):
    return(np.log(v)/np.log(base))
logs = log_np(hall_vect, base)
radius = 200
points_in_semi_circle = 100

hallway_steepness = .8
door_bottom_x = 300

paths_x = []
paths_y = []

for i in logs:
    # Generate points along a semicircle
    theta = np.linspace(0, np.pi, points_in_semi_circle)
    noise_d_x = 3
    noise_d_y = 6
    semi_x = np.sin(theta)*(radius - i*1.2) - i + 100 - .5*i
    semi_y = np.cos(theta)*(radius - i*1.2) - i
    #noise_door_frame = np.array([noise.noise2(x/noise_d_x, y/noise_d_y) + .5 for x,y in zip(semi_x,semi_y)])*.5
    #paths_x.append(scale*(semi_x) + log_np(noise_door_frame, base) + offset_x)
    paths_x.append(scale*(semi_x) + offset_x)
    paths_y.append(scale*(semi_y) + offset_y)
    # add points for the bottom of the door
    paths_x[-1][0] = (i*hallway_steepness)*scale + door_bottom_x
    paths_x[-1][-1] = (i*hallway_steepness)*scale + door_bottom_x


last_door = Polygon([(x,y) for x,y in zip(paths_x[-1], paths_y[-1])])

hall_turn_increment = 4
for j in range(10):
    i = logs[-1]
    # Generate points along a semicircle
    theta = np.linspace(0, np.pi, points_in_semi_circle)
    xs = scale*(np.sin(theta)*(radius - i*1.2) - i + 100 - .5*i) + offset_x
    ys = scale*(np.cos(theta)*(radius - i*1.2) - i + hall_turn_increment*j) + offset_y
    pts = [Point(x,y) for x,y in zip(xs,ys)]
    xs_occ = np.array([x for x,pt in zip(xs,pts) if last_door.contains(pt)])
    ys_occ = np.array([y for y,pt in zip(ys,pts) if last_door.contains(pt)])
    if len(xs_occ) > 0:
        paths_x.append(xs_occ)
        paths_y.append(ys_occ)
        # add points for the bottom of the door
        paths_x[-1][-1] = door_bottom_x + i*hallway_steepness

f = open("door2.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

last_door_idx = len(logs)-1

start_path(f, 0, 0)
add_point(f, X_BOUND-1, Y_BOUND-1)
add_point(f, 0, Y_BOUND-1)
add_point(f, 0, 0)
close_path(f)

# write paths to svg file
for xs,ys in zip(paths_x,paths_y):
    start_path(f, xs[0], ys[0])
    for x,y in zip(xs[1:], ys[1:]):
        add_point(f, x, y)
    if np.array_equal(xs,paths_x[last_door_idx]) or np.array_equal(xs,paths_x[0]):
        add_point(f, xs[0], ys[0])
    close_path(f)


# connect all door bottoms right
start_path(f, paths_x[0][0], paths_y[0][0])
add_point(f, paths_x[last_door_idx][0], paths_y[last_door_idx][0])
close_path(f)

# connect all door bottoms left
start_path(f, paths_x[0][-1], paths_y[0][-1])
add_point(f, paths_x[last_door_idx][-1], paths_y[last_door_idx][-1])
close_path(f)

f.write('</svg>\n')

# Close the file
f.close()
