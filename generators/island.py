import math
import pprint

# How many blocks deep to raise
depth = 32

# How many blocks to raise the surface
# 134 will move sea level to the highest cloud level
height = 133
height_relative = True

def block_center(block):
    """Return the coordinate corresponding to a block index.

    The center of the block at (x,y,z) is (x+0.5, y+0.5, z+0.5).
    """
    return block + 0.5

def coord_to_block(coord):
    """
    Return the block index corresponding to the coordinate.
    """
    assert(coord >= 0)
    return int(round(coord - 0.5))

def get_fill_rectangles(block_radius, y0=-1, height=1):
    
    y_top = y0 + height - 1
    
    rectangles = []
    previous_z_block = None
    previous_fill_x = None
    
    for x_block in range(block_radius + 1):

        if x_block < block_radius:
            x = block_center(x_block)
            z = math.sqrt(block_radius*block_radius - x*x)

            # The index of the last block is the block count - 1
            z_block = int(round(z)) - 1
        else:
            # Finishes drawing the last row
            z_block = -1

        if previous_z_block is not None and previous_z_block != z_block:
            # z_block has changed, fill a rectangle using previous x, z
            if previous_fill_x is None:
                rectangles.append( (
                    (-previous_x_block - 1, y0, -previous_z_block - 1),
                    (previous_x_block, y_top, previous_z_block)
                ))
                previous_fill_x = previous_x_block
            else:
                # Positive x
                rectangles.append( (
                    (previous_fill_x + 1, y0, -previous_z_block - 1),
                    (previous_x_block, y_top, previous_z_block)
                ))
                # Negative x
                rectangles.append( (
                    (-previous_x_block - 1, y0, -previous_z_block - 1),
                    (-previous_fill_x - 2, y_top, previous_z_block)
                ))
                previous_fill_x = previous_x_block

        previous_x_block = x_block
        previous_z_block = z_block
    return rectangles

rectangles = []
for y in range(depth):
    radius = int(math.floor(y / 4)) + 1
    rectangles += get_fill_rectangles(radius, -depth + y)
rectangles += get_fill_rectangles(8, 0, 32)

#pprint.pp(rectangles)

for rectangle in rectangles:
    height_str = str(rectangle[0][1] + height)
    if height_relative:
        height_str = "~" + height_str
    command = "clone ~{} ~{} ~{} ~{} ~{} ~{} ~{} {} ~{}".format(
        rectangle[0][0], rectangle[0][1], rectangle[0][2],
        rectangle[1][0], rectangle[1][1], rectangle[1][2],
        rectangle[0][0], height_str, rectangle[0][2])
    print(command)
    
rectangles = get_fill_rectangles(8, -1)
