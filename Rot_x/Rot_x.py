#Matriz de rotación en el eje "x"

# Import libraries and packages
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# create the fig and ax objects to handle figure and axes of the fixed frame
fig,ax = plt.subplots()

# Use 3d view 
ax = plt.axes(projection = "3d")


def setaxis(x1, x2, y1, y2, z1, z2):
    # this function is used to fix the view to the values of input arguments
    # -----------------------------------------------------------------------
    # ARGUMENTS
    # x1, x2 -> numeric value
    # y1, y2 -> numeric value
    # y1, z2 -> numeric value
    # -----------------------------------------------------------------------
    ax.set_xlim3d(x1,x2)
    ax.set_ylim3d(y1,y2)
    ax.set_zlim3d(z1,z2)
    ax.view_init(elev=30, azim=40)


def fix_system(axis_length):
    # Fix system function 
    # Plots a 3D centered at [x,y,z] = [0,0,0]
    # -------------------------------------------------------------------
    # Arguments 
    # axis_length -> used to specify the length of the axis, in this case
    #                all axes are of the same length
    # -------------------------------------------------------------------
    x = [0, axis_length]
    y = [0, axis_length] 
    z = [0, axis_length]
    zp = [0, 0]
    ax.plot3D(x, zp, zp, color='red') #eje "x" en rojo
    ax.plot3D(zp, y, zp, color='blue') #eje "y" en azul
    ax.plot3D(zp, zp, z, color='green') #eje "z" en verde
    

def sind(t):
    # sind function
    # Computes the sin() trigonometric function in degrees
    # ----------------------------------------------------------------------
    # Arguments
    # t -> Numeric, angle in degrees. 
    # ----------------------------------------------------------------------
    res = np.sin(t*np.pi/180)
    return res

def cosd(t):
    # sind function
    # Computes the cos() trigonometric function in degrees
    # ----------------------------------------------------------------------
    # Arguments
    # t -> Numeric, angle in degrees. 
    # ----------------------------------------------------------------------
    res = np.cos(t*np.pi/180)
    return res

#Matriz de rotación en "x"

def RotX(t):
    Rx = np.array(([1, 0, 0],
                   [0, cosd(t), -sind(t)],
                   [0, sind(t),  cosd(t)]))
    return Rx

#Dibujar vectores

def drawVector(v):
    deltaX = [0, v[0]]
    deltaY = [0, v[1]]
    deltaZ = [0, v[2]]
    ax.plot3D(deltaX, deltaY, deltaZ,color='orange')
    #plt.draw()
    #plt.pause(0.001)

#Animación de la rotación en "x"

def rotateX(t):
    n = 0 #esta es la condición inicial n=0
    while n < t: 
        ax.cla() #se limpia todo
        # Set the view 
        setaxis(0,2,0,2,0,2) #ajusta bien el area del dibujo

        # plot the axis
        fix_system(1) #dibuja los ejes

        # draw vector1
        v1 = np.array([0,0.5,0]) #vector inicial en "y" (para ver la rot.)
        drawVector(v1)

        # draw vector2
        v2 = RotX(n).dot(v1) #para rotar el vector "n" grados
        drawVector(v2) 

        n = n + 1 #sumar un grado para ver el movimiento
        plt.draw()
        plt.pause(0.001) #para pausar y ver el vector moviendose

rotateX(45) #gira 90° alrededor del eje X

#show image
plt.draw()
plt.show()