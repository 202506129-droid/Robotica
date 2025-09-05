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
    ax.plot3D(zp, y, zp, color='green',linewidth=linewidth)
    ax.plot3D(zp, zp, z, color='blue',linewidth=linewidth)

def sind(t): return np.sin(t*np.pi/180)
def cosd(t): return np.cos(t*np.pi/180)

def TRy(t):
    Ry = np.array([[cosd(t), 0, sind(t), 0],
                   [0, 1, 0, 0],
                   [-sind(t), 0, cosd(t), 0],
                   [0, 0, 0, 1]])
    return Ry

def TRz(t):
    Rz = np.array([[cosd(t),-sind(t),0,0],
                   [sind(t), cosd(t),0,0],
                   [0,0,1,0],
                   [0,0,0,1]])
    return Rz

def TTx(L):
    Tx = np.array([[1,0,0,L],
                   [0,1,0,0],
                   [0,0,1,0],
                   [0,0,0,1]])
    return Tx

def drawVector(p_fin, p_init=[0,0,0], color='black',linewidth=1):
    deltaX = [p_init[0], p_fin[0]]
    deltaY = [p_init[1], p_fin[1]]
    deltaZ = [p_init[2], p_fin[2]]
    ax.plot3D(deltaX, deltaY, deltaZ,color=color, linewidth=linewidth)

def drawMobileFrame(origin, x, y, z):
    x = [(origin[0] + x[0]), (origin[1] + x[1]), (origin[2] + x[2])]
    y = [(origin[0] + y[0]), (origin[1] + y[1]), (origin[2] + y[2])]
    z = [(origin[0] + z[0]), (origin[1] + z[1]), (origin[2] + z[2])]

    drawVector(x,origin, color="red")
    drawVector(y,origin, color="green")
    drawVector(z,origin, color="blue")

def getUnitaryVectorsFromMatrix(TM):
    x      = [TM[0][0], TM[1][0], TM[2][0]]
    y      = [TM[0][1], TM[1][1], TM[2][1]]
    z      = [TM[0][2], TM[1][2], TM[2][2]]
    origin = [TM[0][3], TM[1][3], TM[2][3]]
    return[x,y,z,origin]

# --------------------------
# Ajustes de escena
# --------------------------
setaxis(-20,20,-20,20,-20,20)
fix_system(10,linewidth=1)

# Parámetros del robot
alpha1 = 30   # rotación base sobre Y
theta1 = 40
theta2 = 30
theta3 = 20
L1, L2, L3 = 8, 6, 4

# --------------------------
# Cinemática
# --------------------------
A = TRy(alpha1)
B = TRz(theta1); C = TTx(L1)
D = TRz(theta2); E = TTx(L2)
F = TRz(theta3); G = TTx(L3)

T1 = A
[x1,y1,z1,origin1] = getUnitaryVectorsFromMatrix(T1)
drawMobileFrame(origin1, x1, y1, z1)

T2 = T1.dot(B).dot(C)
[x2,y2,z2,origin2] = getUnitaryVectorsFromMatrix(T2)
drawMobileFrame(origin2, x2, y2, z2)
drawVector(origin2, origin1, color="black", linewidth=3)

T3 = T2.dot(D).dot(E)
[x3,y3,z3,origin3] = getUnitaryVectorsFromMatrix(T3)
drawMobileFrame(origin3, x3, y3, z3)
drawVector(origin3, origin2, color="black", linewidth=3)

T4 = T3.dot(F).dot(G)
[x4,y4,z4,origin4] = getUnitaryVectorsFromMatrix(T4)
drawMobileFrame(origin4, x4, y4, z4)
drawVector(origin4, origin3, color="black", linewidth=3)

# Mostrar resultado
plt.show()
