"""
                                    SHAPE & TEXT
"""

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
# img[height,width]
# img[200:300,100:300] = 255,0,0
cv2.line(img, (0,0), (300,300),(0,255,0),3)
cv2.line(img, (0,300), (300,0),(0,255,0),3)
cv2.rectangle(img, (0,0),(300,300),(255,0,0),3)
# cv2.rectangle(img, (0,0),(300,300),(255,0,0), cv2.FILLED)
cv2.circle(img,(150,150),146,(0,0,255),3)

cv2.putText(img,"  HARSH  ",(85,335),cv2.FONT_ITALIC,1,(0,150,0))




cv2.imshow("blank", img)
cv2.waitKey(0)