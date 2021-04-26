import cv2
import numpy as np

framewidth = 1920
frameheight = 1080
cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,130)

mycolors = [[105,122,60,156,238,255]]

mycolorvalues = [[255,0,255]]

mypoints = []

def findcolor(img, mycolors, mycolorvalues):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for colors in mycolors:
        lower = np.array(colors[0:3])
        upper = np.array(colors[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        x,y = getcontours(mask)
        cv2.circle(imgresult, (x,y),10,mycolorvalues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newpoints.append([x,y, count])
            count+=1
        # cv2.imshow("find color", mask)
    return  newpoints


def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>50:
            cv2.drawContours(imgresult, cnt, -1, (255,255,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2, y

def drawoncanvas(mypoints, mycolorvalues):
    for point in mypoints:
        cv2.circle(imgresult, (point[0], point[1]),10,mycolorvalues[point[2]],cv2.FILLED)



while True:
    success, img = cap.read()
    imgresult = img.copy()
    newpoints = findcolor(img, mycolors, mycolorvalues)
    if len(newpoints)!=0:
        for newp in newpoints:
            mypoints.append(newp)

    if len(newpoints)!=0:
        drawoncanvas(mypoints, mycolorvalues)

    cv2.imshow("result", imgresult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
