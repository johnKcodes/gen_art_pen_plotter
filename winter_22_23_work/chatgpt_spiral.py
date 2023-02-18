import math

# Image size (pixels)
IMG_SIZE = (1350, 1060)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]

# The number of turns in the spiral
TURNS = 20

# The number of points in the spiral
N_POINTS = 100

# The maximum radius of the spiral
MAX_RADIUS = 200

# The line color
LINE_COLOR = "#000000"

# The line width
LINE_WIDTH = 2

# The gap between the edge of the image and the spiral
MARGIN = 50

# The starting point of the spiral
START_X = IMG_SIZE[0] / 2
START_Y = IMG_SIZE[1] / 2

# Calculate the angle increment for each point in the spiral
angle_increment = TURNS * 2 * math.pi / N_POINTS

# Create the SVG file
svg_file = open("spiral.svg", "w")

# Write the SVG header
svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

# Set the starting point
x = START_X
y = START_Y

# Write the starting point
svg_file.write('<path d="M {},{}'.format(x, y))

# Create the spiral
for i in range(N_POINTS):
    # Calculate the angle
    angle = angle_increment * i

    # Calculate the radius
    radius = 2*(MAX_RADIUS * angle / (TURNS * 2 * math.pi))

    # Calculate the next point
    x = START_X + radius * math.cos(angle)
    y = START_Y + radius * math.sin(angle)

    # Draw a line to the next point
    svg_file.write(' L {},{}'.format(x, y))

# Close the path
svg_file.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

# Write the SVG footer
svg_file.write('</svg>\n')

# Close the file
svg_file.close()
