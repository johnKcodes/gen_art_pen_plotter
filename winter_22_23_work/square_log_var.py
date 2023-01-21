import math
import vnoise
noise = vnoise.Noise()
import numpy as np
from scipy import stats

# Image size (pixels)
IMG_SIZE = (1400, 1200)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]

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

# rotation
theta = -.5

offset_x = 500
offset_y = 500

n_files = 1

svgs = []
for f in range(n_files):
    svgs.append(open("log_square_var_" + str(f) + ".svg", "w"))
    svgs[-1].write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))


def close_path(f):
    svgs[f].write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(f, x, y):
    svgs[f].write('<path d="M {},{}'.format(x, y))

def add_point(f, x, y):
    svgs[f].write(' L {},{}'.format(x, y))

section_size = 150
base = 1.013
pts_per_sect = 25
x = [math.log(i, base) for i in np.linspace(1, base**section_size, pts_per_sect, endpoint=True)]
xs = np.array([i if i > 0 else .1 for i in x])
ys = np.zeros(len(x))


f = 0

def rotate_x(x, y, theta = 1):
    return(math.cos(theta)*x - math.sin(theta)*y)

def rotate_y(x, y, theta = 1):
    return(math.sin(theta)*x + math.cos(theta)*y)

def stripe(f, xs, ys, thetas = [0]):
        for x,y in zip(xs,ys):
            for t in thetas:
                x1 = rotate_x(y, x, theta = t)
                y1 = rotate_y(y, x, theta = t)
                x2 = rotate_x(x, y, theta = t)
                y2 = rotate_y(x, y, theta = t)
                if t == thetas[0]:
                    start_path(f, offset_x + x1, offset_y + y1)
                add_point(f, offset_x + x2, offset_y + y2)
            close_path(f)
            f += 1
            f = f % n_files

def stripe_outer(f, xs, ys, thetas = [0]):
        for x,y in zip(xs,ys):
            for t in thetas:
                x1 = rotate_x(y, x, theta = t)
                y1 = rotate_y(y, x, theta = t)
                x2 = rotate_x(x, y, theta = t)
                y2 = rotate_y(x, y, theta = t)
                start_path(f, offset_x + x1, offset_y + y1)
                add_point(f, offset_x + x2, offset_y + y2)
                close_path(f)
            f += 1
            f = f % n_files

# for t in [0,math.pi*.5]:
#     def stripe_t(f,x,y,theta = t):
#         stripe(f,x,y,theta)

Y = np.concatenate(
    (ys,ys,ys,ys,xs,
    (section_size*2 - xs)[::-1],
    section_size*2 + xs,
    (section_size*4 - xs)[::-1]
    ),
    axis = 0)*.7
X = np.concatenate(
    (xs,
    (section_size*2 - xs)[::-1],
    section_size*2 + xs,
    (section_size*4 - xs)[::-1],
    section_size*4 + ys,
    section_size*4 + ys,
    section_size*4 + ys,
    section_size*4 + ys
    ),
    axis = 0)*.7

n = len(Y)
h = int(n/2)
stripe(f, Y[:h], X[:h], [0, math.pi*.5, math.pi, math.pi*1.5])
stripe_outer(f, Y[h:], X[h:], [0, math.pi*.5, math.pi, math.pi*1.5])

for f in svgs:
    # Write the SVG footer
    f.write('</svg>\n')

    # Close the file
    f.close()
