##imageStitcher 2
##adds images together vertically given a constant width, height can change theorectically

from PIL import Image as img
xRange = 300
yRange = 40
imgOut = img.new("RGB", (xRange,yRange)) ##make a blank image to output to
files = [] ##list to hold the images the program opens
offset = 0  ##y offset from the previous image added

for i in range(8): ##Open all 8 files
    files.append(img.open(str(i)))
    
for currentImage in files: ##For every image
    for pixelX in range(currentImage.width): ##For every x coord in image
        for pixelY in range(currentImage.height): ##Go through each column
            ##              | Co-ords      | Colour
            imgOut.putpixel((pixelX,pixelY+offset),(currentImage.getpixel((pixelX,pixelY))))
            ##Get the pixel in the source, and put it in the output
    offset = offset + currentImage.height ##Change the y offset so that the next image is below the last one
imgOut.show() ##Output
