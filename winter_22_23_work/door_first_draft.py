import numpy as np
import matplotlib.pyplot as plt
import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


LINE_COLOR = "#000000"
IMG_SIZE = (1400, 1200)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]
LINE_WIDTH = 2
offset_x = 600
offset_y = 400

def close_path(f):
    f.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(f, x, y):
    f.write('<path d="M {},{}'.format(x, y))

def add_point(f, x, y):
    f.write(' L {},{}'.format(x, y))

base = 1.031
n_doors = 50
logs = (np.log(np.linspace(1, 100**base, n_doors))/np.log(base))
radius = 200

paths_x = []
paths_y = []

for i in logs[::-1]:
# Generate 10 points along a semicircle
    theta = np.linspace(0, np.pi, 100)
    paths_x.append(np.sin(theta)*(radius - i*1.2) - i + 100 - .5*i + offset_x)
    paths_y.append(np.cos(theta)*(radius - i*1.2) - i + offset_y)
    paths_x[-1][0] = 300 + i*.3
    paths_x[-1][-1] = 300 + i*.3

last_door = Polygon([(x,y) for x,y in zip(paths_x[-1], paths_y[-1])])

f = open("door.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

for xs,ys in zip(paths_x,paths_y):
    start_path(f, xs[0], ys[0])
    for x,y in zip(xs[1:], ys[1:]):
        add_point(f, x, y)
    if all(xs == paths_x[-1]) or all(xs == paths_x[0]):
        add_point(f, xs[0], ys[0])
    close_path(f)

for i in range(5):
    start_path(f, xs[0], ys[0])
    for x,y in zip(xs[1:], ys[1:]):
        add_point(f, x, y)
    if all(xs == paths_x[-1]) or all(xs == paths_x[0]):
        add_point(f, xs[0], ys[0])
    close_path(f)

# connect all door bottoms right
start_path(f, paths_x[0][0], paths_y[0][0])
add_point(f, paths_x[-1][0], paths_y[-1][0])
close_path(f)

# connect all door bottoms left
start_path(f, paths_x[0][-1], paths_y[0][-1])
add_point(f, paths_x[-1][-1], paths_y[-1][-1])
close_path(f)

f.write('</svg>\n')

# Close the file
f.close()
