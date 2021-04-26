"""
                                       functions
"""

import cv2
import numpy as np

img = cv2.imread("./Photos/cat.jpg")
kernal = np.ones((5,5), np.uint8)

imggrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggrey, (9,9), 4)
imgcanny = cv2.Canny(img,150,200)
imgdilation = cv2.dilate(imgcanny, kernal, iterations=1)
imgeroded = cv2.erode(imgdilation, kernal,iterations=1)

# cv2.imshow("grey image", imggrey)
# cv2.imshow("blur image", imgblur)
cv2.imshow("canny image", imgcanny)
cv2.imshow("dilate image", imgdilation)
cv2.imshow("erode image", imgeroded)
cv2.waitKey(0)