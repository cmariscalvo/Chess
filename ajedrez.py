# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:50:09 2021

@author: Christian Mariscal
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

'Funcion: Coge una casilla del tablero y la compara con la pieza que quieras, sacando la norma de la matriz diferencia de ambas imagenes'
def clasificacion(name,parte):
    nombre = plt.imread(name)
    alto,ancho,colores = parte.shape
    nombre=cv2.resize(nombre,(ancho,alto))
    'Importante. El resize hacerlo de la imagen más pequeña a la más grande para no perder resolucion'
    diferencia = cv2.subtract(parte,nombre)
    norma = np.linalg.norm(diferencia)
    return norma

'Lectura de la imagen del tablero'
inicio = plt.imread('inicio.png')
alto,ancho,colores=inicio.shape
inicio = cv2.resize(inicio,(1360,1360))

'Lista de normas almacena las normas de cada figura con la casilla a comparar'
lista_normas = []

'Cambio de directorio para almacenar las figuras'
os.chdir('C:\\Users\\Christian Mariscal\\Desktop\\ajedrez\\FIGURAS')
piezas = ['caballo_n_n.png','caballo_b_n.png','caballo_n_b.png','caballo_b_b.png','torre_n_n.png','torre_n_b.png','torre_b_n.png','torre_b_b.png','peon_n_n.png','peon_b_b.png','peon_b_n.png','peon_n_b.png','alfil_n_n.png','alfil_b_b.png','alfil_n_b.png','alfil_b_n.png','rey_n_n.png','rey_b_b.png','rey_b_n.png','rey_n_b.png','reina_n_n.png','reina_b_b.png','reina_b_n.png','reina_n_b.png','casilla_b.png','casilla_n.png']

'Creacion de lista de casillas'
alphabet = 'ABCDEFGH'
nombre_casilla = []
lista_casillas=[]
lado=170

for i in range(0,8):
    for j in range(0,8): 
        nombre_casilla =alphabet[i] + str(j+1)
        lista_casillas.append(nombre_casilla)
'x,y,k,z son los límites de la casilla a comparar'        
x=lado*0
y=lado*1
k=lado*7
z=lado*8    
contador = 0
diccionario_juego={}

for casilla in lista_casillas:
    
    contador+=1
    nombre_casilla=casilla
    casilla = inicio[k:z,x:y]
    
    lista_normas = []
    for element in piezas: 
    
       lista_normas.append( clasificacion(element,casilla) )
       
    minimo = min(lista_normas)
    indice = lista_normas.index(minimo)
    diccionario_juego[nombre_casilla] = piezas[indice]
    
    k-=lado
    z-=lado
   
    if contador == 8:
        x+=lado
        y+=lado
        contador = 0
        k = lado*7
        z = lado*8
  
      
