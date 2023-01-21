import math
import vnoise
noise = vnoise.Noise()
import numpy as np
from scipy import stats

# Image size (pixels)
IMG_SIZE = (1400, 800)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]

door_left = 300
door_right = 700
door_bot = 600

semi_radius = 200
semi_x = 200
semi_y = 200

# The number of lines/waves
N_LINES = 20

# The line color
LINE_COLOR = "#000000"

# The line width
LINE_WIDTH = 2

# The gap between the edge of the image and the spiral
MARGIN = 50

# Calculate the angle increment for each point in the spiral
init_step_size = (X_BOUND*.8)/N_LINES

svgs = []
for f in range(1):
    svgs.append(open("door_" + str(f) + ".svg", "w"))
    svgs[-1].write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

def close_path(f = 0):
    svgs[f].write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(x, y, f = 0):
    svgs[f].write('<path d="M {},{}'.format(int(x), int(y)))

def add_point(x, y, f = 0):
    svgs[f].write(' L {},{}'.format(x, y))

section_size = 150
base = 1.013
pts_per_sect = 50
x = [math.log(i, base) for i in np.linspace(1, base**section_size, pts_per_sect, endpoint=False)]
xs = np.array([math.log(i, base) for i in np.linspace(1, base**section_size, pts_per_sect, endpoint=False)])

offset = 100
f = 0

def stripe(f, xs,ys):
    for xs in zip(xs,ys):
        start_path(offset + y, offset + x)
        add_point(offset + x, offset + y)
        close_path()
        f += 1
        f = f % 3

#stripe(f, ys, xs)
def semi_circle(thetas, h = 200, k = 200, r = 200):
    res = [[math.cos(t)*r + h for t in thetas], [math.sin(t)*r + k for t in thetas]]
    return([np.array(a) for a in res])

def under_frame(x,y):
    frame_y = (semi_radius**2 - (x - semi_x)**2)**.5 + semi_y
    return frame_y > y

def in_door(x,y):
    if x > door_left and x < door_right and x > door_bot:
        if under_frame(x,y):
            return(true)

rads = np.linspace(0, math.pi, pts_per_sect, endpoint=False)
pts = semi_circle(rads)

start_path(offset + pts[0][0], offset + pts[0][1])
for x,y in zip(pts[0],pts[1]):
    add_point(offset + x, offset + y)
close_path()

mid = int(len(xs)/2) + 1
for x,y in zip(xs[0:mid],ys[0:mid]):
    start_path(offset + x, offset + y)
    add_point(offset + 400 - x, offset + y)
    close_path()

for f in svgs:
    # Write the SVG footer
    f.write('</svg>\n')
    # Close the file
    f.close()
