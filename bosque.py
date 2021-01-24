import random
import numpy as np

# genera un bosque sano
def generar_bosque(n):
    bosque=[0]*n
    return bosque

# propagacion aleatoria de arboles
def brotes(bosque, p):
    i=0
    while i<len(bosque):
        num= random.random()
        if num < p:
            bosque[i]=1
        i= i+1

# calcula cantidad de arboles de un tipo de celda indicado.
def cuantos(bosque, tipo_celda):
    a=0
    suma=0
    while a<len(bosque):
        if bosque[a]==tipo_celda:
            suma= suma+1
        a=a+1
    return suma

#otra forma de resolverlo seria
    #def cuantos(bosque, tipo_celda):
        #a=0
        #bosque.count()

# quema de arboles de forma aleatoria.
# bosque: vector de arboles
# f: numero elegido de forma aleatoria.
def rayos(bosque, f):
    r=0
    while r<len(bosque):
        num= random.random()
        if num<f:
            if bosque[r]==1:
                bosque[r]=-1
        r=r+1

# mide propagacion del incendio. De existir arbol sano entre dos quemados, se considera quemado por propagación del fuego
def propagacion(bosque):
    p=0
    while p<len(bosque)-1:
        if bosque[p]==-1:
            if bosque[p+1]==1:
                bosque[p+1]=-1
        p=p+1
    s=len(bosque)-1
    while s>0:
        if bosque[s]==-1:
            if bosque[s-1]==1:
                bosque[s-1]=-1
        s=s-1

# restaura el bosque.
def limpieza(bosque):
    l=0
    while l<len(bosque):
        if bosque[l]==-1:
            bosque[l]=0
        l=l+1

print("bosque:")
bosque1=generar_bosque(10)
print(bosque1)

print("arboles nacidos:")
brotes(bosque1, 0.6)
print(bosque1)


cuantos_brotes=cuantos(bosque1, 1)
print("cantidad de arboles encontrados: " + str(cuantos_brotes))

print("rayos:")
rayos(bosque1, 0.5)
print(bosque1)

print("propagacion:")
propagacion(bosque1)
print(bosque1)

print("bosque limpio")
limpieza(bosque1)
print(bosque1)
