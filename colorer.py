import png
import numpy as np
from PIL import Image
import subprocess
import argparse
import matplotlib

img = []

def rgb_tuple(s):
    if s.startswith('#'):
        return hex_to_rgb(s)
    else:
        try:
            red, green, blue = map(int, s.split(','))
            return red, green, blue
        except:
            raise argparse.ArgumentTypeError("Tuples must be red,green,blue")

def hex_to_rgb(hexcolor):
    color = hexcolor.lstrip('#')
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgbcolor):
    colors = rgbcolor.split(',')
    red = colors[0]
    green = colors[1]
    blue = colors[2]
    return '#%02x%02x%02x' % (red, green, blue)

# rainbow gradient
# height and width must be 255 for rgb 255
def rainbow_gradient(output_path):
    for y in range(255):
        row = ()
        for x in range(255):
            row = row + (x, max(0, 255 - x - y), y)
        img.append(row)
    im = Image.fromarray(img)
    im.save(output_path)
    # with open(output_path, 'wb') as f:
    #     w = png.Writer(255, 255, greyscale=False)
    #     w.write(f, img)

def vertical_gradient(height, width, gradient_r_range, gradient_g_range, gradient_b_range, output_path):
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + (gradient_r_range[y], gradient_g_range[y], gradient_b_range[y])
        img.append(row)
    with open(output_path, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

def solid_color(height, width, solid_color, output_path):
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + solid_color
        img.append(row)
    with open(output_path, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

def horizontal_gradient(height, width, gradient_width_r_range, gradient_width_g_range, gradient_width_b_range, output_path):
    for y in range(height):
        h_row = ()
        for x in range(width):
            h_row = h_row + (gradient_width_r_range[x], gradient_width_g_range[x], gradient_width_b_range[x])
        img.append(h_row)
    with open(output_path, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

def concat_h(im1, im2, output_path):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.save(output_path)

def concat_v(im1, im2, output_path):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    dst.save(output_path)

# need to extend color gradient
def diagonal_gradient():
    for y in range(height):
        d_row = ()
        for x in range(width):
            d_row = d_row + (gradient_r_range[min(254, y + x)], gradient_g_range[min(254, y + x)], gradient_b_range[min(254, y + x)])
        img.append(d_row)
    with open('diagonal_gradient2.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Python3 Image Transformer',
        usage="askew.py [-o output] [--height] [--width] [--mode] [-c first_color] [-k second_color] [-i first_image_path] [-e second_image_path]")
    parser.add_argument('-o', dest="output_path", action="store", metavar='output_path',
                        type=str, help="output image path", required=True)
    parser.add_argument('-i', dest="first_image_path", action="store", metavar='first_image_path',
                        type=str, help="first input image path")
    parser.add_argument('-e', dest="second_image_path", action="store", metavar='second_image_path',
                        type=str, help="second input image path")
    parser.add_argument('--mode', dest="mode", metavar='mode',
                        type=str, help="v for vertical gradient, s for solid color, h for horizontal gradient, cv for concatenate vertically, ch for concatenate horizontally", required=True)
    parser.add_argument('--height', metavar='height', type=int,
                        help='set height of output image', required=True)
    parser.add_argument('--width', metavar='width', type=int,
                        help='set width of the output image', required=True)
    parser.add_argument('-c', dest="first_color", metavar='first_color', type=rgb_tuple,
                        help='first color in gradient')
    parser.add_argument('-k', dest="second_color", metavar='second_color', type=rgb_tuple,
                        help='second color in gradient')

    options = parser.parse_args()

    mode = options.mode

    if mode == 'ch':
        if options.first_image_path is None or  options.second_image_path is None:
            raise ValueError('Please provide two images to concatenate')
        im1 = Image.open(options.first_image_path)
        im2 = Image.open(options.second_image_path)
        concat_h(im1, im2, options.output_path)

    elif mode == 'cv':
        if options.first_image_path is None or  options.second_image_path is None:
            raise ValueError('Please provide two images to concatenate')
        im1 = Image.open(options.first_image_path)
        im2 = Image.open(options.second_image_path)
        concat_v(im1, im2, options.output_path)

    elif mode == 'r':
        rainbow_gradient(options.output_path)

    elif mode == 'v':
        rgb_1 = options.first_color
        rgb_2 = options.second_color
        gradient_r_range = np.linspace(rgb_1[0], rgb_2[0], options.height, dtype = int)
        gradient_g_range = np.linspace(rgb_1[1], rgb_2[1], options.height, dtype = int)
        gradient_b_range = np.linspace(rgb_1[2], rgb_2[2], options.height, dtype = int)
        vertical_gradient(
            options.height,
            options.width,
            gradient_r_range,
            gradient_g_range,
            gradient_b_range,
            options.output_path
        )

    elif mode == 'h':
        rgb_1 = options.first_color
        rgb_2 = options.second_color
        gradient_width_r_range = np.linspace(rgb_1[0], rgb_2[0], options.width, dtype = int)
        gradient_width_g_range = np.linspace(rgb_1[1], rgb_2[1], options.width, dtype = int)
        gradient_width_b_range = np.linspace(rgb_1[2], rgb_2[2], options.width, dtype = int)
        horizontal_gradient(
            options.height,
            options.width,
            gradient_width_r_range,
            gradient_width_g_range,
            gradient_width_b_range,
            options.output_path
        )

    elif mode == 's':
        solid_color(options.height, options.width, options.first_color, options.output_path)

    else:
        raise ValueError('mode not recongnized')


    # extended_gradient_r_range = np.linspace(rgb_1[0], rgb_2[0], height * 2, dtype = int)
    # extended_gradient_g_range = np.linspace(rgb_1[1], rgb_2[1], height * 2, dtype = int)
    # extended_gradient_b_range = np.linspace(rgb_1[2], rgb_2[2], height * 2, dtype = int)
