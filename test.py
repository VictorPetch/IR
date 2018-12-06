import cv2
import numpy as np
import cv2   as cv

def printCoordinates(event,x,y,flags,func):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Teu cu',x,y)

def preencher(mtx,x,y):
    #print('working')
    value = mtx[x,y]
    h,w = mtx.shape[:2]
    mtx = np.c_[ np.zeros(h), mtx, np.zeros(h) ]
    mtx = np.r_[ np.zeros((1,w+2)), mtx,np.zeros((1,w+2))]
    x = x+1
    y = y+1
    if(mtx[x+1,y] == 0):
        mtx[x+1,y] = value +1 
    if(mtx[x,y+1] == 0):
        mtx[x,y+1] = value +1
    if(mtx[x-1,y] == 0):
        mtx[x-1,y] = value +1
    if(mtx[x,y-1] == 0):
        mtx[x,y-1] = value +1
    return mtx[1:h+1,1:w+1]

print('luiz',cv2.imread('images/Suamae.jpg'))
image = cv2.imread('images/Suamae.jpg')

cv2.imshow('detected circles',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=31,param2=30,minRadius=8,maxRadius=37)
circles = np.uint16(np.around(circles))
print(circles)
xi,yi = 0,0
xf,yf = 0,0
mapa = np.zeros((480,640),dtype=np.uint8)
for i in circles[0,:]:
    if(i[1] <= 180):
        #r = 0;
        #b = 255;
        #g = 0;
        #Tam = 28;
        xi,yi = i[0],i[1]

    elif(i[1] > 286 ):
        #r = 255;
        #b = 0;
        #g = 0;
        #Tam = 78;
        xf,yf = i[0],i[1]
    elif(i[0] > 550 ):
        pass
        #r = 0;
        #b = 0;
        #g = 0;
        #Tam = 24;
    else:
        r = 255;
        b = 255;
        g = 255;
        Tam = 24;
        cv2.circle(image,(i[0],i[1]),1,(b,g,r),Tam)
    # draw the outer circle
    #cv2.circle(image,(i[0],i[1]),i[2],(b,g,r),2)
    # draw the center of the circle
    #cv2.circle(image,(i[0],i[1]),2,(b,g,r),3)
    #print(i)
    # fill the circles
    #cv2.circle(image,(i[0],i[1]),1,(b,g,r),Tam)

#cv2.imshow('detected circles',image)
#cv2.imwrite('area_51.jpeg',image)

#cv2.setMouseCallback('detected circles',printCoordinates)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

mapa[110:113,110:113] = 255 
#mapa[0:4,6:8] = 255 

cv2.imshow('detected circles',mapa)
cv2.waitKey(0)

mapa = preencher(mapa,100,100)
h,w = mapa.shape[:2]
cont,i,j = 0,0,0
while (mapa[120][120] == 0):
    cont+=1
    

    for i in range(0,h):
        
        for j in range(0,w):
            
            if(mapa[i,j] == cont and mapa[i,j] != 255 ):
                mapa = preencher(mapa,i,j)
    print('ie j ',mapa[120][120])

    cv2.imshow('depois',mapa)
    cv2.waitKey(1)
mapa[100,100] = 0
cv2.imshow('depois',mapa)
cv2.waitKey(0)
mapa = np.c_[ np.ones(h)*255, mapa, np.ones(h)*255 ]
mapa = np.r_[ np.ones((1,w+2))*255, mapa,np.ones((1,w+2))*255]
qini = mapa[430,100] 

print(mapa[98:121,98:121])





#mapa = mapa + image

cv2.imshow('depois',mapa)
cv2.waitKey(0)

