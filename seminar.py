import cv2
import numpy

def myThresholdFunction(img, channel, threshold):
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (img[i][j][channel] < threshold):
                img[i][j] = [0,0,0]
            else:
                img[i][j] = [255,255,255]
    return img

def histogram(img, img2):
    
    #array for storing values
    results = []
    for i in range(256):
        results.append([0,0,0])
        
    #storing every BGR tone value to array
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                results[img[i][j][k]][k] += 1
                
    maximum = numpy.amax(results)
    #reducing all values to fit in 256x256 image
    for i in range(256):
        for j in range(3):
            results[i][j] = results[i][j]*256/maximum

    #drawing image by changing channel values of certain pixels        
    for i in range(256):
        for j in range(3):
            for k in range(results[i][j]):
                img2[255-k][i][j] = 255
    return img2

cv2.namedWindow("Sample")
img = cv2.imread("RBG.jpg")
img2 = numpy.zeros((256,256,3), numpy.uint8)

img2 = histogram(img, img2)
#myThresholdFunction(img, 2, 100)
cv2.imshow("Sample", img)
cv2.imshow("Sample2", img2)
while True:    
    ch = cv2.waitKey(5)
    # Kill program when ESC pressed
    if ch == 27:
        break
cv2.destroyAllWindows()

