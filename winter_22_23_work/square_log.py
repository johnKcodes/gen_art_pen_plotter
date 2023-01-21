import math
import vnoise
noise = vnoise.Noise()
import numpy as np
from scipy import stats

# Image size (pixels)
IMG_SIZE = (1400, 800)
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

svgs = []
for f in range(3):
    svgs.append(open("log_square_" + str(f) + ".svg", "w"))
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

offset = 100

f = 0

def stripe(f, xs,ys):
    for x,y in zip(xs,ys):
        start_path(f, offset + y, offset + x)
        add_point(f, offset + x, offset + y)
        close_path(f)
        f += 1
        f = f % 3

stripe(f, ys, xs)
stripe(f, ys, reversed(section_size*2 - xs))
stripe(f, ys, section_size*2 + xs)
stripe(f, ys, reversed(section_size*4 - xs))
stripe(f, xs, section_size*4 + ys)
stripe(f, reversed(section_size*2 - xs), section_size*4 + ys)
stripe(f, section_size*2 + xs, section_size*4 + ys)
stripe(f, reversed(section_size*4 - xs), section_size*4 + ys)

for f in svgs:
    # Write the SVG footer
    f.write('</svg>\n')

    # Close the file
    f.close()
