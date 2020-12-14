import cv2
import numpy

im_g = cv2.imread("img.jpg",1)

print(numpy.flip(im_g))
cv2.imwrite("newimg.png",numpy.flip(im_g))