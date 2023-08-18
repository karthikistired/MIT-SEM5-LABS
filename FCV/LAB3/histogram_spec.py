import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the source and target images
img= cv.imread("C:\\Users\\OS LAB\\Pictures\\Camera Roll\\monalisa.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


gray_hist=cv.calcHist([gray],[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
#plt.xlim([0,256])
plt.show()


plt.figure()
plt.title('colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)

