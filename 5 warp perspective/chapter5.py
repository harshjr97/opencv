"""
                                      WARP PERSPECTIVE
"""
import cv2
import numpy as np

img = cv2.imread("Photos/cards.jpg")

width, height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image", img)
cv2.imshow("image Perspective", imgoutput)
cv2.waitKey()