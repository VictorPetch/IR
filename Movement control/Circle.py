import cv2
import numpy as np
import cv2   as cv

image = cv2.imread('images/Essedacerto.jpg')
cv2.imshow('detected circles',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=35,maxRadius=50)
circles = np.uint16(np.around(circles))


for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)
    print("Circle:", i)

cv2.imshow('detected circles',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
