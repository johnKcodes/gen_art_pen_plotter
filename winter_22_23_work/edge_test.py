
def close_path(f):
    f.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

def start_path(f, x, y):
    f.write('<path d="M {},{}'.format(x, y))

def add_point(f, x, y):
    f.write(' L {},{}'.format(x, y))

axi_error_scale = 305/246
IMG_SIZE = (1152*axi_error_scale, 864*axi_error_scale)
X_BOUND = IMG_SIZE[0]
Y_BOUND = IMG_SIZE[1]
LINE_COLOR = "black"
LINE_WIDTH = 1

f = open("edge_test.svg", "w")
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

start_path(f, 0, 0)
add_point(f, X_BOUND-1, 0)
add_point(f, X_BOUND-1, Y_BOUND-1)
add_point(f, 0, Y_BOUND-1)
add_point(f, 0, 0)
close_path(f)

f.write('</svg>\n')

# Close the file
f.close()
