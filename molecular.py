import numpy as np
import random

def rebotar (pos, vel, minimo, maximo):
    if pos > maximo:
        vel = -vel
        pos = pos - 2 * (pos - maximo)
    if pos < minimo:
        vel = -vel
        pos = pos - 2 * (pos - minimo)
    return pos, vel

def mover_particula (pos_x, pos_y, vel_x, vel_y, dt, x_min, x_max, y_min, y_max):
    i=0
    while i < len(pos_x):
        pos_x[i] = pos_x[i] + vel_x[i] *dt
        pos_y[i] = pos_y[i] + vel_y[i] * dt
        pos_x[i],vel_x[i]=rebotar(pos_x[i], vel_x[i], x_min, x_max)
        pos_y[i],vel_y[i]=rebotar(pos_y[i], vel_y[i], y_min, y_max)
        i= i+1
    return pos_x, pos_y, vel_x, vel_y

def escribir_frame(archivo, pos_x, pos_y, nparts):
    print (nparts,file = archivo )
    print (" ",file = archivo )
    for i in range (nparts):
        print ("6", pos_x[i] , pos_y[i] , "0", file = archivo )
    
def calcula_distcuadrada(x_1, y_1, x_2, y_2):
    dist_cuadrada= np.sqrt ((x_1 - x_2)**2 + (y_1 - y_2)**2)
    return dist_cuadrada

def calcular_fuerzas(pos_x, pos_y):
    Fx=[0]*len(pos_x)
    Fy=[0]*len(pos_y)
    for i in range (nparts):
        for j in  range(nparts):
           if i != j:
              Fx[i] += 4 * k * (pos_x[i] - pos_x[j]) / calcula_distcuadrada(pos_x[i], pos_y[i], pos_x[j], pos_y[j])**3
              Fy[i] += 4 * k * (pos_y[i] - pos_y[j]) / calcula_distcuadrada(pos_x[i], pos_y[i], pos_x[j], pos_y[j])**3
    return Fx, Fy
              
def aplicar_fuerzas(vel_x, vel_y, Fx, Fy, masas, dt):
    for i in range (len(masas)): 
        vel_x= vel_x + (Fx[i] / masas[i])* dt
        vel_y= vel_y + (Fy[i] / masas[i])* dt
    return vel_x, vel_y

  
#defino valores de la caja
x_min=0
x_max=20
y_min=0
y_max=20

#defino posicion inicial de la particula
pos_x=[2, 5, 9, 20, 32, 40, 55] 
pos_y=[3, 6, 10, 22, 35, 45, 50]
    
#defino velocidad en X e Y
vel_x=[2, 1, 1.5, 3, 2, 1, 2.5 ]
vel_y=[3, 2.5, 1, 3, 2, 1.5, 2]

#defino dt y pasos_totales
dt= 0.001
pasos_totales= 10000

#defino valor de k
k=1    

#defino valor de masas
masas=[1]*len(pos_x)

#defino num de particulas
nparts=7  

archivo= open ("salida.xyz", "w")

for i in range(pasos_totales):
    pos_x, pos_y, vel_x, vel_y=mover_particula (pos_x, pos_y, vel_x, vel_y, dt, x_min, x_max, y_min, y_max)
    if (i %100) == 0:
        escribir_frame(archivo, pos_x, pos_y, nparts) 
    
archivo . close ()