import matplotlib.pyplot as plt
import numpy as np

def cinematica_directa(theta1, theta2, a1, a2):

    # Base en el origen
    base = np.array([0, 0, 0])

    # Primer eslabón: apuntando hacia arriba (eje Z)
    joint1 = np.array([
        a1 * np.sin(theta1),
        0,
        a1 * np.cos(theta1)
    ])

    # Segundo eslabón: gira en el plano XZ
    end_effector = joint1 + np.array([
        a2 * np.sin(theta1 + theta2),
        0,
        a2 * np.cos(theta1 + theta2)
    ])

    return base, joint1, end_effector

def dibujar_robot(ax, base, joint1, ef):
    #Dibuja el robot 3D en posición vertical
    xs = [base[0], joint1[0], ef[0]]
    ys = [base[1], joint1[1], ef[1]]
    zs = [base[2], joint1[2], ef[2]]
    ax.plot(xs, ys, zs, '-o', color='black', linewidth=3)
    ax.scatter(xs, ys, zs, color='red', s=40)

# ANIMACIÓN

def animar(theta1_final, theta2_final, a1, a2):
    pasos = 80
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(pasos + 1):
        ax.cla()
        ax.set_xlim(-a1 - a2, a1 + a2)
        ax.set_ylim(-a1 - a2, a1 + a2)
        ax.set_zlim(0, a1 + a2)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.view_init(elev=30, azim=45)
        ax.set_title("Robot 3D de pie (movimiento en plano XZ)")

        # Interpolación de ángulos
        t = i / pasos
        th1 = np.deg2rad(theta1_final * t)
        th2 = np.deg2rad(theta2_final * t)

        base, joint1, ef = cinematica_directa(th1, th2, a1, a2)
        dibujar_robot(ax, base, joint1, ef)

        plt.pause(0.05)

    plt.show()

if __name__ == "__main__":
    print("Simulación 3D de robot 2 eslabones en posición vertical")

    a1 = float(input("Ingrese longitud del primer eslabón (a1): "))
    a2 = float(input("Ingrese longitud del segundo eslabón (a2): "))
    theta1 = float(input("Ingrese ángulo θ1 (en grados): "))
    theta2 = float(input("Ingrese ángulo θ2 (en grados): "))

    animar(theta1, theta2, a1, a2)
