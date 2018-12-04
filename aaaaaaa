import cv2
import numpy as np
import cv2   as cv

def printCoordinates(event,x,y,flags,func):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Teu cu',x,y)


image = cv2.imread('images/Suamae.jpg')

cv2.imshow('detected circles',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=31,param2=30,minRadius=8,maxRadius=37)
circles = np.uint16(np.around(circles))
xi,yi = 0,0
xf,yf = 0,0
image = np.zeros((480,640))
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

cv2.imshow('detected circles',image)
cv2.imwrite('area_51.jpeg',image)

cv2.setMouseCallback('detected circles',printCoordinates)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Essa parte calcula o trajeto da solucao
def preencher(mtx,x,y):
    value = mtx[x,y]
    h,w = mtx.shape[:2]
    mtx = np.c_[ np.zeros(h), mtx, np.zeros(h) ]
    mtx = np.r_[ np.zeros((1,w+2)), mtx,np.zeros((1,w+2))]
    x = x+1
    y = y+1
    if(mtx[x+1,y] == 0)     :
        mtx[x+1,y] = value +1
    if(mtx[x,y+1] == 0):
        mtx[x,y+1] = value +1
    if(mtx[x-1,y] == 0):
        mtx[x-1,y] = value +1
    if(mtx[x,y-1] == 0):
        mtx[x,y-1] = value +1
    return mtx[1:h+1,1:w+1]

mapa = image

#cv2.imshow('area_51',mapa)
#cv2.waitKey(0)

#mapa = np.zeros((32,32),dtype=np.uint8)

#mapa[3:6,2:4] = 255
#mapa[0:4,6:8] = 255

#mapa = preencher(mapa,384,312)
h,w = mapa.shape[:2]
cont = 0
mapa[443,170] =
while (False):
    cont+=1
    for i in range(0,h):
        for j in range(0,w):
            if(mapa[i,j] == cont and mapa[i,j] != 255 ):
                pass
                #mapa = preencher(mapa,i,j)


#mapa = np.c_[ np.ones(h)*255, mapa, np.ones(h)*255 ]
#mapa = np.r_[ np.ones((1,w+2))*255, mapa,np.ones((1,w+2))*255]
qini = mapa[443,170]
qfin = mapa[384,312]
manhatam.




#mapa = mapa + image

cv2.imshow('depois',imagem)
cv2.waitKey()


while((xp is not 443)and (yp is not 170)):
    value = mapa[xp,yp]
    print('Estou no ponto:',xp,yp,'Valor:',value)
    if(mapa[xp +1,yp]<value ):
        xp=xp+1
    elif(mapa[xp -1,yp]<value ):
        xp=xp-1
    elif(mapa[xp,yp+1]<value ):
            yp=yp+1
    elif(mapa[xp,yp-1]<value ):
        yp=yp-1
    else:
        print(mapa[xp +1,yp],mapa[xp -1,yp],mapa[xp,yp +1],mapa[xp,yp -1])
    mapa[xp,yp] = 0

    cv2.imshow('detected circles',mapa)
    cv2.waitKey()
