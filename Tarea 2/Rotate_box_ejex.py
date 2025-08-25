
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

def fix_system(axis_length, linewidth=5):
    x = [-axis_length, axis_length]
    y = [-axis_length, axis_length] 
    z = [-axis_length, axis_length]
    zp = [0, 0]
    ax.plot3D(x, zp, zp, color='red', linewidth=linewidth)
    ax.plot3D(zp, y, zp, color='blue',linewidth=linewidth)
    ax.plot3D(zp, zp, z, color='green',linewidth=linewidth)

def sind(t):
    res = np.sin(t*np.pi/180)
    return res

def cosd(t):
    res = np.cos(t*np.pi/180)
    return res


def RotX(t):
    Rx = np.array(([1,0,0],
                   [0,cosd(t),-sind(t)],
                   [0,sind(t), cosd(t)]))
    return Rx

def drawVector(p_fin, p_init=[0,0,0], color='black',linewidth=1):
    deltaX = [p_init[0], p_fin[0]]
    deltaY = [p_init[1], p_fin[1]]
    deltaZ = [p_init[2], p_fin[2]]
    ax.plot3D(deltaX, deltaY, deltaZ,color=color, linewidth=linewidth)

def drawBox(p1, p2, p3, p4, p5, p6, p7, p8, color = 'black'):
    
    drawScatter(p1)
    drawScatter(p2)
    drawScatter(p3)
    drawScatter(p4)
    drawScatter(p5)
    drawScatter(p6)
    drawScatter(p7)
    drawScatter(p8)
    
    drawVector(p1,p2,color = color)
    drawVector(p2,p3,color = color)
    drawVector(p3,p4,color = color)
    drawVector(p4,p1,color = color)
    drawVector(p5,p6,color = color)
    drawVector(p6,p7,color = color)
    drawVector(p7,p8,color = color)
    drawVector(p8,p5,color = color)
    drawVector(p4,p8,color = color)
    drawVector(p1,p5,color = color)
    drawVector(p3,p7,color = color)
    drawVector(p2,p6,color = color)

def drawScatter(point,color='black',marker='o'):
    ax.scatter(point[0],point[1],point[2],marker='o')

def rotate_box(p1,p2,p3,p4,p5,p6,p7,p8,axis='z', angle = 0):
    rotation_matrix = 0
    if axis=='x': 
        rotation_matrix = RotX(angle) 
    if axis=='y':
        pass
    if axis=='z':
        pass

    p1_rot = rotation_matrix.dot(p1)
    p2_rot = rotation_matrix.dot(p2)
    p3_rot = rotation_matrix.dot(p3)
    p4_rot = rotation_matrix.dot(p4)
    p5_rot = rotation_matrix.dot(p5)
    p6_rot = rotation_matrix.dot(p6)
    p7_rot = rotation_matrix.dot(p7)
    p8_rot = rotation_matrix.dot(p8)

    return [p1_rot,p2_rot,p3_rot,p4_rot,p5_rot,p6_rot,p7_rot,p8_rot]

# Puntos iniciales de la caja
p1_init = np.array([0,0,0])
p2_init = np.array([7,0,0])
p3_init = np.array([7,0,3])
p4_init = np.array([0,0,3])
p5_init = np.array([0,2,0])
p6_init = np.array([7,2,0])
p7_init = np.array([7,2,3])
p8_init = np.array([0,2,3])

# Animación de la rotación en X
def animate_rotation_x(grados=90):
    n = 0
    while n < grados:
        ax.cla()  # limpiar
        setaxis(-5,5,-5,5,-5,5)
        fix_system(10,1)

        # Caja inicial en negro
        drawBox(p1_init,p2_init,p3_init,p4_init,
                p5_init,p6_init,p7_init,p8_init,color='black')

        # Caja rotada en rojo
        [p1_rot, p2_rot, p3_rot, p4_rot,
         p5_rot, p6_rot, p7_rot, p8_rot] = rotate_box(p1_init,p2_init,p3_init,p4_init,
                                                      p5_init,p6_init,p7_init,p8_init,
                                                      axis='x', angle=n)

        drawBox(p1_rot,p2_rot,p3_rot,p4_rot,
                p5_rot,p6_rot,p7_rot,p8_rot,color='red')

        n += 1
        plt.draw()
        plt.pause(0.01)

animate_rotation_x(90)
plt.show()
