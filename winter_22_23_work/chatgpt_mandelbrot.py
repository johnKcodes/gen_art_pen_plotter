
import numpy as np
import matplotlib.pyplot as plt

# The maximum number of iterations
MAX_ITER = 256

# The image size (pixels)
IMG_SIZE = (400, 400)

# The plot limits
PLOT_LIMS = (-2, 1, -1.5, 1.5)

# Create the complex plane
X, Y = np.meshgrid(
    np.linspace(PLOT_LIMS[0], PLOT_LIMS[1], IMG_SIZE[0]),
    np.linspace(PLOT_LIMS[2], PLOT_LIMS[3], IMG_SIZE[1])
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
ax.imshow(N, cmap=cmap, interpolation='none', extent=PLOT_LIMS)

# Save the plot
plt.savefig('mandelbrot.png', dpi=150)
