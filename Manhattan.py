#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def preencher(mtx,x,y):
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

mapa = np.zeros((32,32),dtype=np.uint8)


mapa[3:6,2:4] = 255 
mapa[0:4,6:8] = 255 

mapa = preencher(mapa,1,1)
h,w = mapa.shape[:2]
cont = 0
while (0 in mapa):
    cont+=1
    for i in range(0,h):
        for j in range(0,w):
            if(mapa[i,j] == cont and mapa[i,j] != 255 ):
                mapa = preencher(mapa,i,j)
mapa[1,1] = 0 
mapa = np.c_[ np.ones(h)*255, mapa, np.ones(h)*255 ]
mapa = np.r_[ np.ones((1,w+2))*255, mapa,np.ones((1,w+2))*255]
qini = mapa[5,8] 
