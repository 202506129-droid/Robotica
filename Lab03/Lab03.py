#LAB_03


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
    ax.plot3D(x, zp, zp, color='red')
    ax.plot3D(zp, y, zp, color='blue')
    ax.plot3D(zp, zp, z, color='green')
    

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


def RotZ(t):
    Rz = np.array(([cosd(t),-sind(t),0],[sind(t),cosd(t),0],[0,0,1]))
    return Rz

def drawVector(v):
    deltaX = [0, v[0]]
    deltaY = [0, v[1]]
    deltaZ = [0, v[2]]
    ax.plot3D(deltaX, deltaY, deltaZ,color='orange')
    #plt.draw()
    #plt.pause(0.001)

def rotate(t):
    n = 0 # SE DEFINE N=0 COMO CONDICION INCIAL
    while n < t: 
        ax.cla() #LIMPIA LA PANTALLA, ES DECIR ANTES D DIBUJAR SE BORRA TODO
        # Set the view 
        setaxis(0,2,0,2,0,2) # PONE BIEN LA CAMARA

        # plot the axis
        fix_system(1) #DIBUJA LOS EJES

        # draw vector1
        v1 = np.array([2,0,0]) #DIBUJA EL VECTOR
        drawVector(v1)

        # draw vector2
        v2 = RotZ(n).dot(v1) #ROTO EL VECTOR N GRADOS
        drawVector(v2) #DIBUJO EL VECTOR

        n = n + 1 # LE SUMO UN GRADO A LOS GRADOS PA ASI CUANDO SE BORRE Y SE VUELVA A DIBUJAR ES COMO SI SE HUBIERA MOVIDO
        plt.draw()
        plt.pause(0.001) #PARA Q SE PAUSE Y SE PUEDA VER EL EFECTO D Q SE ESTA MOVIENDO





rotate(45) #AQUI ESTAS PONIENDO CUANTO ES t, SE VA A MOVER HASTA LOS GRADOS Q PONGAS AQUI, EN ESTE CASO SON 45ºTU


# show image.
plt.draw()
plt.show()