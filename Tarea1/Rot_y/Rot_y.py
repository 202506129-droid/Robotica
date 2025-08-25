#Matriz de rotación en el eje "y"

# Import libraries and packages
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# create the fig and ax objects to handle figure and axes of the fixed frame
fig,ax = plt.subplots()

# Use 3d view 
ax = plt.axes(projection = "3d")


def setaxis(x1, x2, y1, y2, z1, z2):
    ax.set_xlim3d(x1,x2)
    ax.set_ylim3d(y1,y2)
    ax.set_zlim3d(z1,z2)
    ax.view_init(elev=30, azim=40)


def fix_system(axis_length):
    x = [0, axis_length]
    y = [0, axis_length] 
    z = [0, axis_length]
    zp = [0, 0]
    ax.plot3D(x, zp, zp, color='red')   # eje X en rojo
    ax.plot3D(zp, y, zp, color='blue')  # eje Y en azul
    ax.plot3D(zp, zp, z, color='green') # eje Z en verde
    

def sind(t):
    return np.sin(t*np.pi/180)

def cosd(t):
    return np.cos(t*np.pi/180)

#Matriz de rotación en "y"
def RotY(t):
    Ry = np.array(([cosd(t), 0, sind(t)],
                   [0, 1, 0],
                   [-sind(t), 0, cosd(t)]))
    return Ry

#Dibujar vectores
def drawVector(v):
    deltaX = [0, v[0]]
    deltaY = [0, v[1]]
    deltaZ = [0, v[2]]
    ax.plot3D(deltaX, deltaY, deltaZ, color='orange')

#Animación de la rotación en "y"
def rotateY(t):
    n = 0 
    while n < t: 
        ax.cla() 
        setaxis(0,2,0,2,0,2) 
        fix_system(1) 

        # vector inicial (en Z para que se vea bien la rotación en Y)
        v1 = np.array([0,0,0.5]) 
        drawVector(v1)

        # vector rotado
        v2 = RotY(n).dot(v1) 
        drawVector(v2) 

        n = n + 1 
        plt.draw()
        plt.pause(0.001) 

rotateY(45) # gira 45° alrededor del eje Y

#show image
plt.draw()
plt.show()
