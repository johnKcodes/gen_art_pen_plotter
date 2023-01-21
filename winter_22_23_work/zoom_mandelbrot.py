
import numpy as np
import matplotlib.pyplot as plt
import random

# The maximum number of iterations
MAX_ITER = 256

# The image size (pixels)
IMG_SIZE = (400, 400)

# The plot limits
PLOT_LIMS = (-2, 1, -1.5, 1.5)

# The number of images to generate
N_IMAGES = 30

# The zoom factor for each image
ZOOM_FACTOR = 0.5

# Generate random coordinates for the center of the zoom
center_x = random.uniform(PLOT_LIMS[0], PLOT_LIMS[1])
center_y = random.uniform(PLOT_LIMS[2], PLOT_LIMS[3])

# Calculate the width and height of each image
img_width = (PLOT_LIMS[1] - PLOT_LIMS[0]) / (ZOOM_FACTOR ** N_IMAGES)
img_height = (PLOT_LIMS[3] - PLOT_LIMS[2]) / (ZOOM_FACTOR ** N_IMAGES)

# Iterate over the images
for i in range(N_IMAGES):
    # Calculate the plot limits for the current image
    x_lims = (center_x - img_width / 2, center_x + img_width / 2)
    y_lims = (center_y - img_height / 2, center_y + img_height / 2)

    # Create the complex plane
    X, Y = np.meshgrid(
        np.linspace(x_lims[0], x_lims[1], IMG_SIZE[0]),
        np.linspace(y_lims[0], y_lims[1], IMG_SIZE[1])
    )

    # Convert the complex plane to complex numbers
    C = X + Y * 1j

    # Create an array to store the iterations for each point
    Z = np.zeros_like(C)

    # Create an array to store the number of iterations for each point
    N = np.zeros_like(C, dtype=np.int)

    # Iterate over the complex plane
    for n in range(MAX_ITER):
        I = np.less(abs(Z), 2)
        N[I] = n
        Z[I] = Z[I] ** 2 + C[I]

    # Create a colormap
    cmap = plt.cm.hot

    # Set the limits of the color map
    cmap.set_bad('#000000', 1.)

    # Create the plot
    fig, ax = plt.subplots()
    ax.imshow(N, cmap=cmap, interpolation='none', extent=x_lims + y_lims)

    # Save the plot
    plt.savefig('mandelbrot_{}.png'.format(i), dpi=150)

    # Zoom in on the center for the next image
    center_x +=
