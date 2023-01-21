
import math

# Set the size of the image
IMAGE_SIZE = (500, 500)

# Set the number of cycles in the sine wave
NUM_CYCLES = 10

# Set the starting point of the sine wave
START_POINT = (250, 250)

# Set the line width of the sine wave
LINE_WIDTH = 5

# Set the line color of the sine wave
LINE_COLOR = "black"

# Set the filename to save the image to
FILENAME = "sine_wave.svg"

# Calculate the step size for the sine wave based on the number of cycles
# and the size of the image
step_size = IMAGE_SIZE[0] / NUM_CYCLES

# Open the file for writing
with open(FILENAME, "w") as f:
    # Write the SVG header
    f.write('<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(IMAGE_SIZE[0], IMAGE_SIZE[1]))

    # Set the starting point of the sine wave
    x, y = START_POINT

    # Write the starting point of the sine wave
    f.write('<path d="M{},{} '.format(x, y))

    # Create the sine wave by plotting points along the x-axis
    # and calculating the y-coordinate using the sine function
    for i in range(0, IMAGE_SIZE[0], step_size):
        x += step_size
        y = START_POINT[1] + math.sin(x * math.pi * 2 / IMAGE_SIZE[0] * NUM_CYCLES) * IMAGE_SIZE[1] / 2
        f.write('L{},{} '.format(x, y))

    # Close the path and set the line properties
    f.write('" stroke="{}" stroke-width="{}" fill="none" />\n'.format(LINE_COLOR, LINE_WIDTH))

    # Write the SVG footer
    f.write('</svg>\n')
