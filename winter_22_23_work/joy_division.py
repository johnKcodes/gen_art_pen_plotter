import math
import vnoise
noise = vnoise.Noise()
from scipy import stats

gaussian = stats.norm.pdf

noise_d_x = 30
noise_d_y = 60
noise_mult = 25000

# Image size (pixels)
IMG_SIZE = (1400, 800)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]

# The number of lines/waves
N_LINES = 100

# The number of points per line
N_POINTS = 500

# The line color
LINE_COLOR = "#000000"

# The line width
LINE_WIDTH = 2

# The gap between the edge of the image and the spiral
MARGIN = 50

# The starting point of the spiral
START_X = 0
START_Y = 0

# Calculate the angle increment for each point in the spiral
init_step_size = (X_BOUND*.8)/N_LINES

# Create the SVG file
svg_file = open("joy_division.svg", "w")

# Write the SVG header
svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

# Set the starting point
x = START_X
y = START_Y

frontier_x = []

def close_path():
    svg_file.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path():
    svg_file.write('<path d="M {},{}'.format(x, y))

start = False

# Create the spiral
for i in range(N_LINES):

    for j in range(N_POINTS):
        x = init_step_size*i
        # Calculate the next point
        y = Y_BOUND/N_POINTS*j
        frac_from_cent = (Y_BOUND/2 - abs(Y_BOUND/2 - y))**4/(Y_BOUND/2)
        g = gaussian(y,Y_BOUND/2,60)
        noise_contrib1 = (noise.noise2(x/noise_d_x, y/noise_d_y) + .5) * g * noise_mult
        noise_contrib2 = (noise.noise2(x/20, y/20) + .5) * 3
        x = x + noise_contrib1 + noise_contrib2

        if i == 0:
            frontier_x.append(x)

        if i != 0 and x < frontier_x[j]:
            close_path()
            start = True
            continue
        else:
            frontier_x[j] = x

        # Draw a line to the next point
        if j == 0 or start:
            start_path()
            start = False
        else:
            svg_file.write(' L {},{}'.format(x, y))

    close_path()

# Write the SVG footer
svg_file.write('</svg>\n')

# Close the file
svg_file.close()
