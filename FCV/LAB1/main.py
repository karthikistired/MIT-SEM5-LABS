import cv2
img_grayscale=cv2.imread('C:\\Users\\OS LAB\\Pictures\\Camera Roll\\the-blank-signature.jpg',0)
cv2.imshow('grayscale image',img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('D:\\grayscaleee.jpg',img_grayscale)