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


def fix_system(axis_length, linewidth=5):
    # Fix system function 
    # Plots a 3D centered at [x,y,z] = [0,0,0]
    # -------------------------------------------------------------------
    # Arguments 
    # axis_length -> used to specify the length of the axis, in this case
    #                all axes are of the same length
    # -------------------------------------------------------------------
    x = [-axis_length, axis_length]
    y = [-axis_length, axis_length] 
    z = [-axis_length, axis_length]
    zp = [0, 0]
    ax.plot3D(x, zp, zp, color='red', linewidth=linewidth)
    ax.plot3D(zp, y, zp, color='blue',linewidth=linewidth)
    ax.plot3D(zp, zp, z, color='green',linewidth=linewidth)

def mobile_frame(origin, x, y, z):
    # This function draws a movile frame 
    #--------------------------------------------------------------------
    xx = x[0]
    xy = x[1]
    xz = x[2]
    

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

def TRx(t):
    Rx = 0
    return Rx

def TRy(t):
    Ry = 0
    return Ry

def TRz(t):
    Rz = np.array(([cosd(t),-sind(t),0, 0],[sind(t),cosd(t),0, 0],[0,0,1, 0], [0,0,0,1]))
    return Rz

def TTx(t):
    Tx = 0
    return Tx

def TTy(t):
    Ty = 0
    return Ty

def TTz(t):
    Tz = np.array(([1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, t],[0,0,0,1]))
    return Tz

def drawVector(p_fin, p_init=[0,0,0], color='black',linewidth=1):
    deltaX = [p_init[0], p_fin[0]]
    deltaY = [p_init[1], p_fin[1]]
    deltaZ = [p_init[2], p_fin[2]]
    ax.plot3D(deltaX, deltaY, deltaZ,color=color, linewidth=linewidth)


def drawMobileFrame(origin, x, y, z):
    drawVector(x,origin, color="red")
    drawVector(y,origin, color="green")
    drawVector(z,origin, color="blue")
  
# Set the view 
setaxis(-15,15,-15,15,-15,15)

# plot the axis
fix_system(10,linewidth=1)




# show image.
plt.draw()
plt.show()



