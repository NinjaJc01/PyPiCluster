from PIL import Image as img
import picalc
##((300*5)*6 is range of n)
##9000 digits per node
nodeIDfile = open("id.txt","r")
xRange = 300
yRange = 5
imgOut = img.new("RGB", (xRange,yRange)) ##make a blank image to output to
nodeID = int(nodeIDfile.read())
print(nodeID)
range_ = xRange * yRange


def placePixel(colourCode,x,y):
    r = int(colourCode[:2], 16)
    g = int(colourCode[2:4], 16)
    b = int(colourCode[4:6], 16)
    #print([r,g,b])
    imgOut.putpixel((x,y),(r,g,b))

currentDigit = nodeID*range_

for yVal in range(yRange):
    for xVal in range(xRange):
        colourVal = (picalc.pi(currentDigit)[:6])
        placePixel(colourVal, xVal, yVal)
        currentDigit = currentDigit+1
imgOut.save(str(nodeID), "png")

        

    
    
