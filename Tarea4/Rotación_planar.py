import matplotlib.pyplot as plt
import numpy as np

# FUNCIONES DE CINEMÁTICA

def directa(ang1, ang2, L1, L2):
    #Devuelve posiciones de base, codo y efector final. 
    x_codo = L1 * np.cos(ang1)
    y_codo = L1 * np.sin(ang1)
    x_ef = x_codo + L2 * np.cos(ang1 + ang2)
    y_ef = y_codo + L2 * np.sin(ang1 + ang2)
    return (0,0), (x_codo,y_codo), (x_ef,y_ef)

def inversa(px, py, L1, L2, modo="arriba"):
    #Calcula los ángulos del brazo para llegar a (px,py).
    r = np.hypot(px, py)
    if r > L1 + L2 or r < abs(L1 - L2):
        return None  # punto inalcanzable

    # Ley del coseno
    cos_theta2 = (px**2 + py**2 - L1**2 - L2**2) / (2*L1*L2)
    cos_theta2 = np.clip(cos_theta2, -1, 1)
    theta2 = np.arccos(cos_theta2)

    # Dos posibles soluciones
    if modo == "arriba":
        theta2 = -theta2
    else:
        theta2 = +theta2

    k1 = L1 + L2 * np.cos(theta2)
    k2 = L2 * np.sin(theta2)
    theta1 = np.arctan2(py, px) - np.arctan2(k2, k1)

    return theta1, theta2

# DIBUJO

def dibuja_brazo(ax, ang1, ang2, L1, L2, destino=None):
    #Dibuja el brazo y opcionalmente marca el destino.
    base, codo, ef = directa(ang1, ang2, L1, L2)
    xs = [base[0], codo[0], ef[0]]
    ys = [base[1], codo[1], ef[1]]
    ax.plot(xs, ys, "-o", color="black", linewidth=3)
    if destino is not None:
        ax.scatter([destino[0]], [destino[1]], c="red", s=60)

def ejes(ax, limite):
    #Dibuja ejes cartesianos
    ax.plot([-limite, limite],[0,0], "r-", lw=1)
    ax.plot([0,0],[-limite, limite], "g-", lw=1)

# ANIMACIÓN

def interpolar(a0, a1, t):
    #Interpolación de ángulos considerando 2π
    return a0 + ((a1 - a0 + np.pi) % (2*np.pi) - np.pi) * t

def animar(L1, L2, px, py, modo="arriba"):
    sol = inversa(px, py, L1, L2, modo)
    if sol is None:
        print("⚠ El punto no se puede alcanzar.")
        return
    ang1_f, ang2_f = sol
    print(f"Ángulos: θ1 = {np.degrees(ang1_f):.2f}°, θ2 = {np.degrees(ang2_f):.2f}°")

    pasos = 80
    ang1_0, ang2_0 = 0.0, 0.0
    lim = L1 + L2 + 1

    fig, ax = plt.subplots(figsize=(6,6))
    for i in range(pasos+1):
        t = i/pasos
        ang1 = interpolar(ang1_0, ang1_f, t)
        ang2 = interpolar(ang2_0, ang2_f, t)
        ax.cla()
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.set_title(f"Brazo 2D - codo {modo}")
        ejes(ax, lim)
        dibuja_brazo(ax, ang1, ang2, L1, L2, destino=(px, py))
        plt.pause(0.03)

    plt.show()

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    print("Brazo planar 2D con codo arriba/abajo")
    modo = input("Modo (arriba/abajo): ").strip().lower()
    if modo not in ["arriba","abajo"]:
        modo = "arriba"
    L1 = float(input("Longitud L1: "))
    L2 = float(input("Longitud L2: "))
    px = float(input("Destino X: "))
    py = float(input("Destino Y: "))
    animar(L1, L2, px, py, modo)
