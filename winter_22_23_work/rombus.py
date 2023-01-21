import math
import vnoise
noise = vnoise.Noise()
from scipy import stats

noise_d_x = 30
noise_d_y = 60
noise_mult = 25000

# Image size (pixels)
IMG_SIZE = (1400, 800)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]

# The number of lines/waves
N_LINES = 20

# The number of points per line
N_POINTS = 500

# The line color
LINE_COLOR = "#000000"

# The line width
LINE_WIDTH = 2

# The gap between the edge of the image and the spiral
MARGIN = 50

# Calculate the angle increment for each point in the spiral
init_step_size = (X_BOUND*.8)/N_LINES

# Create the SVG file
svg_file = open("rombus1.svg", "w")

# Write the SVG header
svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))


def close_path():
    svg_file.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(x, y):
    svg_file.write('<path d="M {},{}'.format(x, y))

def add_point(x,y):
    svg_file.write(' L {},{}'.format(x, y))

x0 = 400
y0 = 100
x1 = 300
y1 = 400
x2 = 400
y2 = 700

# Create the spiral
for i in range(N_LINES):

    start_path(x0,y0)
    add_point(x1,y1)
    add_point(x2,y2)
    close_path()

    x0 += 20
    x1 += 20
    x2 += 20
    
# Write the SVG footer
svg_file.write('</svg>\n')

# Close the file
svg_file.close()

svg_file = open("rombus2.svg", "w")

svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))


x0 = 400
y0 = 100
x1 = 600
y1 = 400
x2 = 400
y2 = 700

# Create the spiral
for i in range(N_LINES):

    start_path(x0,y0)
    add_point(x1,y1)
    add_point(x2,y2)
    close_path()

    x0 += 20
    x1 += 20
    x2 += 20

# Write the SVG footer
svg_file.write('</svg>\n')

# Close the file
svg_file.close()
