# Program that converts a grayscale PNG image to a 4-bit image suitable for
# use on an OLED or something
import png
f = open('702.png', 'rb')      # binary mode is important
r = png.Reader(f)

width = 256
height = 64

outputMatrix = [[0 for x in range(int(width/2))] for y in range(height)]
globalPixel = 0
rowNo = 0
pixelNo = 0

image = r.read()
print(image[3])

pixels = list(image[2])

for row in pixels:
    pixelNo = 0
    for pixel in row:
        if (pixelNo % 2 == 0) :
            scaled = 16*int(pixel/16)
        else :
            scaled = int(pixel/16)
        outputMatrix[rowNo][int(pixelNo/2)] += scaled
        globalPixel += 1
        pixelNo += 1
    rowNo += 1

f.close()

f = open('image_temp.h', 'w')
f.write("uint8_t image_temp[")
f.write(str(height))
f.write("][")
f.write(str(int(width/2)))
f.write("] = {\n")

for i, row in enumerate(outputMatrix) :
    f.write("{")
    for j, byte in enumerate(row) :
        f.write(str(hex(byte)))
        if (j < len(row) - 1) :
            f.write(", ")
    if (i < len(outputMatrix) - 1) :
        f.write("},\n")
f.write("}\n};")
