import math

# The line color
LINE_COLOR = "#000000"

# The line width
LINE_WIDTH = 2

# Image size (pixels)
IMG_SIZE = (1400, 800)
grid_unit = 20
ybounds = [400,grid_unit]

# Create the SVG file
svg_file = open("zigzag.svg", "w")

# Write the SVG header
svg_file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{}" height="{}">\n'.format(IMG_SIZE[0], IMG_SIZE[1]))

# Set the starting point

# Write the starting point
svg_file.write('<path d="M {},{}'.format(0, 0))
obst = set([(0,260),(540,260),(160,ybounds[0]-20),(540,grid_unit),
    (680,ybounds[0]-20),(1060,20),(1060,260),(1060+160-20,ybounds[0]-20)])
#obst = set([(80 + 100*i, 80 + 40*i) for i in range(11)])
path = [(grid_unit,0), (grid_unit,grid_unit), (grid_unit,2*grid_unit)]
dir = [(0,1),(1,0),(0,-1),(1,0)]
diridx = 0
x_incr = grid_unit
y_incr = grid_unit
x = 0
y = 0


# Create the spiral
while x < IMG_SIZE[0]:
    cdir = dir[diridx]

    if (x - x_incr, y) not in path and x != 0 and y not in ybounds:
        print('step left')
        print(x,y)
        x = path[-1][0] - x_incr
        y = path[-1][1]
        print(x,y)
    else:
        print('regular')
        x = path[-1][0] + cdir[0] * x_incr
        y = path[-1][1] + cdir[1] * y_incr

    if (x,y) in obst or (x,y) in path:
        if (x,y) in obst:
            obst.remove((x,y))
        print('side_step')
        x = path[-1][0] + x_incr
        y = path[-1][1]
    elif(y in ybounds):
        print('change dir')
        diridx = (diridx + 1) % 4
    print(x,y)
    path.append((x,y))
    if(y < -10): break

for i,p in enumerate(path):
    if i < 3:
        continue
    if path[i] == path[i-2]:
        path.pop(i-1)
        path.pop(i-2)

for p in path:
    svg_file.write(' L {},{}'.format(p[0], p[1]))


# Close the path
svg_file.write('" fill="none" stroke="{}" stroke-width="{}" />\n'.format(LINE_COLOR, LINE_WIDTH))

# Write the SVG footer
svg_file.write('</svg>\n')

# Close the file
svg_file.close()
