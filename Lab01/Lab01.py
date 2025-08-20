#LAB_01

# Import libraries and packages INSERTAR LIBRERIAS
import matplotlib.pyplot as plt #INSERTAR LIBRERIAS
from mpl_toolkits import mplot3d #INSERTAR LIBRERIAS
import numpy as np #INSERTAR LIBRERIAS

# create the fig and ax objects to handle figure and axes of the fixed frame
fig,ax = plt.subplots() #FIG=VENTANA, AX=EJES

# Use 3d view 
ax = plt.axes(projection = "3d")



def setaxis(x1, x2, y1, y2, z1, z2): #MANEJAR LA VISTA, HACER ZOOMOUT, X1=DESDE DONDE EMPIEZAS A VER A DONDE ACABAS D VER, SUELE SER 0
    # this function is used to fix the view to the values of input arguments
    # -----------------------------------------------------------------------
    # ARGUMENTS
    # x1, x2 -> numeric value
    # y1, y2 -> numeric value
    # y1, z2 -> numeric value
    # -----------------------------------------------------------------------
    ax.set_xlim3d(x1,x2) #Q EL EJE X VA DE X1 A X2
    ax.set_ylim3d(y1,y2)
    ax.set_zlim3d(z1,z2)
    ax.view_init(elev=30, azim=40) #APARTE DE AMPLIAR LA IMAGEN, Q ADEMAS DE COMO PRESPECTIVA


def fix_system(axis_length): #RECIBE DE PARAMETROS UN NUMERO Q ES LA LONJITUD D LOS EJES
    # Fix system function 
    # Plots a 3D centered at [x,y,z] = [0,0,0]
    # -------------------------------------------------------------------
    # Arguments 
    # axis_length -> used to specify the length of the axis, in this case
    #                all axes are of the same length
    # -------------------------------------------------------------------
    x = [0, axis_length] #LONGITUD DE LA LINEA Q SE QUIERE PINTAR, Q IRA DESDE 0 AL NUMERO Q LE DIGAS
    y = [0, axis_length] 
    z = [0, axis_length]
    zp = [0, 0]
    ax.plot3D(x, zp, zp, color='red') #PARA PINTAR LA LINEA, COMO SOLO QUIERES DIBUJAR EN X, A LA Z LE MANDAS 0, Q ES EL COMANDO ANTERIOR A ESTE
    ax.plot3D(zp, y, zp, color='blue')
    ax.plot3D(zp, zp, z, color='green')
    plt.draw() #PARA MOSTRAR LA IMAGEN

def sind(t):
    # sind function
    # Computes the sin() trigonometric function in degrees
    # ----------------------------------------------------------------------
    # Arguments
    # t -> Numeric, angle in degrees. 
    # ----------------------------------------------------------------------
    res = np.sin(t*np.pi/180) #DE GRADOS A RADIANES, T ES LA ROTACION Q SE QUIERE EN GRADOS.
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


# Set the view 
setaxis(0,2,0,2,0,2) #CONFIGURACION DE LA VISTA D LA CAMARA

# plot the axis
fix_system(1) #DIBUJAR LAS LINEAS, CON LONGITUD DE UNA UNIDAD, POR ESO EL 1

# show image.
plt.show() #PARA ASEGURAR EL DIBUJO