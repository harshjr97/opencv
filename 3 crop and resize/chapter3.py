"""
                                    RESIZING & CROPPING
"""
import cv2
import numpy as np

# resize

img = cv2.imread("./Photos/lady.jpg")
print(img.shape)
imgresize = cv2.resize(img, (800,700))


# crop
imgcropped = img[0:200,200:500]

cv2.imshow("cat",img)
# cv2.imshow("catreshape",imgresize)
cv2.imshow("catcropped",imgcropped)
cv2.waitKey(0)


