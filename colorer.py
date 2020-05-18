# from PIL import Image

# im = Image.new("RGB", (800, 1200), '')
# im.save( "color.png", "PNG")

# im = 

# make gradient

# import png

# width = 255
# height = 255
# img = []
# for y in range(height):
#     row = ()
#     for x in range(width):
#         row = row + (x, max(0, 255 - x - y), y)
#     img.append(row)
# with open('gradient.png', 'wb') as f:
#     w = png.Writer(width, height, greyscale=False)
#     w.write(f, img)

import png
import numpy as np

width = 255
height = 255
img = []
for y in range(height):
    row = ()
    for x in range(width):
        row = row + (x, max(0, 255 - x - y), y)
    img.append(row)
with open('gradient.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)