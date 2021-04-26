'''
                                       READ IMAGES - VIDEO - WEBCAMS
'''

import cv2

# read images
# img = cv2.imread("./Photos/cat.jpg")
# cv2.imshow("output", img)
# cv2.waitKey(0)

# read video
# cap = cv2.VideoCapture("Videos/dog.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


# read a webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
