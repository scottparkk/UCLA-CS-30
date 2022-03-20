import struct
import functools

'''
You need to implement the six empty functions defined below.
Each function takes a single argument:
  an image represented as a list of lists of pixels, where
  each pixel is a dictionary as described in the HTML file.
Each function returns a new list in exactly that same form.

The inputPPM and outputPPM functions defined at the end of the file should NOT be
called by your code.  Rather, they are provided to help you test your code:
inputPPM allows you to convert PPM image files into lists of lists of pixels that
can be passed as arguments to your functions, and outputPPM allows you to write the
results of your functions to image files so that the images can be viewed.  See
the HTML file for an example of how to use these functions.

But viewing images is not sufficient!  You should also test as we usually do, by
writing tests to ensure that the output of your function is as expected.  See
hw5test.py.
'''

def nhelper(d):
    return {'r': 255 - d['r'], 'g': 255 - d['g'], 'b': 255 - d['b']}
def negate(pixels): 
    return list(map(lambda x: list(map(nhelper, x)),pixels))

def ghelper(d):
    total = d['r'] + d['g'] + d['b']
    divide = round(total/3)
    return {'r': divide, 'g': divide, 'b': divide}
def greyscale(pixels):
    return list(map(lambda x: list(map(ghelper, x)),pixels))

#def uhelper(d):
#    return
def upsideDown(pixels):
    result = []
    for x in pixels:
        result = [x] + result
    return result
   
#    return functools.reduce(lambda x, elem: elem[::-1] + x, pixels, [])


def mirrorImage(pixels):
#    result = []
#    for x in pixels:
#        for i in x[::-1]:
#            result = result + [i]
#    return result
    result = []
    for inner in pixels:
        s = []
        for x in inner[::-1]:
            s = s + [x]
        result = result + [s]
    return result
            


def compress(pixels):
    result = []
    for inner in pixels[::2]:
        s = []
        for x in inner[::2]:
            s = s + [x]
        result = result + [s]
    return result


def decompress(pixels):
    result = []
    for inner in pixels:
        s = []
        for x in inner:
            s = s + [x] + [x]
        result = result + [s] + [s]
    return result


# input the PPM image file named fname and convert it to a list of lists of pixels.
# each pixel is an RGB triple, represented using a dictionary with keys "r", "g",
# and "b". each list of pixels represents one row in the image, ordered from top to
# bottom.
def inputPPM(fname):
    f = open(fname, "rb")
    p6Ignore = f.readline()
    dimensions = f.readline().split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    maxIgnore = f.readline()

    pixels = []
    rgbData = [x for x in f.read()]
    f.close()
    for r in range(height):
        row = []
        for c in range(width):
            i = 3 * (r * width + c)
            row.append({"r":rgbData[i], "g":rgbData[i+1], "b":rgbData[i+2]})
        pixels.append(row)
    return pixels


# pixels should be a list of list of RGB triples, in the same format as returned
# by the inputPPM function above.
# this function outputs those pixels to the file named fname as a PPM image.
def outputPPM(pixels, fname):
    f = open(fname, "wb")
    f.write("P6\n".encode())
    width = len(pixels[0])
    height = len(pixels)
    f.write((str(width) + " " + str(height) + "\n").encode())
    f.write((str(255) + "\n").encode())
    bPixels = [[struct.pack('BBB', p["r"], p["g"], p["b"]) for p in r] for r in pixels]
    flatPixels = functools.reduce(lambda x,y: x+y, bPixels)
    f.writelines(flatPixels)
    f.close()


