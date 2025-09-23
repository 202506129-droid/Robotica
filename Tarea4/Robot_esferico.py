import matplotlib.pyplot as plt
import numpy as np

#CINEMÁTICA DIRECTA 
def directa(theta_base, theta1, theta2, L1, L2):
    # Devuelve posiciones: base, hombro->codo, codo->efector.
    # Coordenadas en el plano XZ (antes de rotar por la base)
    x_codo = L1 * np.cos(theta1)
    z_codo = L1 * np.sin(theta1)

    x_ef = x_codo + L2 * np.cos(theta1 + theta2)
    z_ef = z_codo + L2 * np.sin(theta1 + theta2)

    # Rotación alrededor del eje Z (theta_base)
    y_codo = 0
    y_ef = 0
    rot = np.array([[np.cos(theta_base), -np.sin(theta_base), 0],
                    [np.sin(theta_base),  np.cos(theta_base), 0],
                    [0,                   0,                  1]])
    codo = rot @ np.array([x_codo, y_codo, z_codo])
    ef   = rot @ np.array([x_ef,   y_ef,   z_ef])

    return np.array([0,0,0]), codo, ef

#CINEMÁTICA INVERSA
def inversa(px, py, pz, L1, L2, modo="arriba"):
    #Calcula ángulos para llegar a (px,py,pz).
    # 1) Ángulo de la base
    theta_base = np.arctan2(py, px)

    # Distancia proyectada en el plano XY
    r = np.hypot(px, py)

    # Reducir a problema 2D en el plano XZ
    X = r
    Z = pz

    dist = np.hypot(X, Z)
    if dist > L1 + L2 or dist < abs(L1 - L2):
        return None

    # Ley del coseno
    cos_theta2 = (X**2 + Z**2 - L1**2 - L2**2) / (2*L1*L2)
    cos_theta2 = np.clip(cos_theta2, -1, 1)
    theta2 = np.arccos(cos_theta2)

    if modo == "arriba":
        theta2 = -theta2
    else:
        theta2 = +theta2

    k1 = L1 + L2 * np.cos(theta2)
    k2 = L2 * np.sin(theta2)
    theta1 = np.arctan2(Z, X) - np.arctan2(k2, k1)

    return theta_base, theta1, theta2

#DIBUJO
def dibuja_brazo(ax, tb, t1, t2, L1, L2, destino=None):
    base, codo, ef = directa(tb, t1, t2, L1, L2)
    xs = [base[0], codo[0], ef[0]]
    ys = [base[1], codo[1], ef[1]]
    zs = [base[2], codo[2], ef[2]]
    ax.plot(xs, ys, zs, "-o", color="black", linewidth=3)
    if destino is not None:
        ax.scatter([destino[0]], [destino[1]], [destino[2]], c="red", s=60)

def ejes(ax, limite=10):
    ax.plot([0,limite],[0,0],[0,0], "r")
    ax.plot([0,0],[0,limite],[0,0], "g")
    ax.plot([0,0],[0,0],[0,limite], "b")

#INTERPOLACIÓN
def interp(a0, a1, t):
    return a0 + ((a1 - a0 + np.pi) % (2*np.pi) - np.pi) * t

#ANIMACIÓN
def animar(L1, L2, px, py, pz, modo="arriba"):
    sol = inversa(px, py, pz, L1, L2, modo)
    if sol is None:
        print("⚠ El punto no se puede alcanzar.")
        return
    tb_f, t1_f, t2_f = sol
    print(f"θ_base={np.degrees(tb_f):.2f}°, θ1={np.degrees(t1_f):.2f}°, θ2={np.degrees(t2_f):.2f}°")

    pasos = 80
    tb0, t10, t20 = 0.0, 0.0, 0.0
    lim = L1 + L2 + 2

    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection="3d")

    for i in range(pasos+1):
        t = i/pasos
        tb = interp(tb0, tb_f, t)
        t1 = interp(t10, t1_f, t)
        t2 = interp(t20, t2_f, t)

        ax.cla()
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_zlim(0, lim)
        ax.set_title(f"Brazo 3D - codo {modo}")
        ejes(ax, lim)
        dibuja_brazo(ax, tb, t1, t2, L1, L2, destino=(px, py, pz))
        plt.pause(0.03)

    plt.show()

#PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("Brazo 3D con codo arriba/abajo")
    modo = input("Modo (arriba/abajo): ").strip().lower()
    if modo not in ["arriba","abajo"]:
        modo = "arriba"
    L1 = float(input("Longitud L1: "))
    L2 = float(input("Longitud L2: "))
    px = float(input("Destino X: "))
    py = float(input("Destino Y: "))
    pz = float(input("Destino Z: "))
    animar(L1, L2, px, py, pz, modo)
