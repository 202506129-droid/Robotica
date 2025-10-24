import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# ------------------ Parámetros del robot ------------------
A1 = 475.0          # Longitud del primer brazo (mm)
A2 = 850.0 - 475.0  # Longitud del segundo brazo (mm)
L3 = 880.0 - 418.5  # Longitud del tercer brazo (mm)
BASE_HEIGHT = 776.0
Z_TRAVEL_MAX = 400.0
R_PLATILLO = 75.0

# ------------------ Matrices DH ------------------
def dh_matrix(a, alpha, d, theta):
    """
    a     : longitud del eslabón
    alpha : ángulo entre ejes z_i y z_{i+1} alrededor de x_i
    d     : desplazamiento a lo largo de z_i
    theta : ángulo de rotación alrededor de z_i
    """
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    
    return np.array([
        [ct, -st*ca,  st*sa, a*ct],
        [st,  ct*ca, -ct*sa, a*st],
        [0,      sa,     ca,    d],
        [0,       0,      0,    1]
    ])

# ------------------ Cinemática directa con DH ------------------
def fkine_dh(theta1, theta2, dz, theta3):
    # Convertir a radianes
    t1 = np.deg2rad(theta1)
    t2 = np.deg2rad(theta2)
    t3 = np.deg2rad(theta3)
    
    # Parámetros DH (SCARA):
    # [a, alpha, d, theta]
    DH_params = [
        [A1, 0, BASE_HEIGHT, t1],
        [A2, 0, 0, t2],
        [0, 0, -dz, 0]  # eslabón 3 vertical (desplazamiento)
    ]
    
    # Transformaciones acumuladas
    T0 = np.eye(4)
    transforms = [T0]
    for a, alpha, d, theta in DH_params:
        T = transforms[-1] @ dh_matrix(a, alpha, d, theta)
        transforms.append(T)
    
    # Extraemos posiciones
    p_base = np.array([0,0,0])
    p_eje = np.array([0,0,BASE_HEIGHT])
    p1 = transforms[1][:3,3]
    p2 = transforms[2][:3,3]
    p3_top = transforms[3][:3,3]
    p3_bottom = p3_top + np.array([0,0,L3])
    
    # Platillo
    angs = np.linspace(0, 2*np.pi, 60)
    circ_x = p3_bottom[0] + R_PLATILLO * np.cos(angs + t3)
    circ_y = p3_bottom[1] + R_PLATILLO * np.sin(angs + t3)
    circ_z = np.ones_like(circ_x) * p3_bottom[2]
    
    # Punto indicador del platillo
    punto_x = p3_bottom[0] + R_PLATILLO * np.cos(t3)
    punto_y = p3_bottom[1] + R_PLATILLO * np.sin(t3)
    punto_z = p3_bottom[2]
    
    return p_base, p_eje, p1, p2, p3_top, p3_bottom, circ_x, circ_y, circ_z, punto_x, punto_y, punto_z

# ------------------ Dibujo ------------------
def dibujar_robot(ax, p_base, p_eje, p1, p2, p3_top, p3_bottom,
                  circ_x, circ_y, circ_z, punto_x, punto_y, punto_z):
    
    ax.scatter(*p_eje, color='black', s=40)
    
    # Primer eslabón - negro
    ax.plot([p_eje[0], p1[0]], [p_eje[1], p1[1]], [p_eje[2], p1[2]], color='black', linewidth=5)
    ax.scatter([p_eje[0], p1[0]], [p_eje[1], p1[1]], [p_eje[2], p1[2]], color='black', s=50)
    
    # Segundo eslabón - gris
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='gray', linewidth=5)
    ax.scatter([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='gray', s=50)
    
    # Tercer eslabón - azul oscuro
    ax.plot([p3_top[0], p3_bottom[0]], [p3_top[1], p3_bottom[1]], [p3_top[2], p3_bottom[2]], color='darkblue', linewidth=4)
    
    # Platillo - azul claro
    ax.plot(circ_x, circ_y, circ_z, color='deepskyblue', linewidth=3)
    
    # Punto indicador platillo - verde claro
    ax.scatter(punto_x, punto_y, punto_z, color='limegreen', s=40)

# ------------------ Animación ------------------
def animar_robot(theta1_f, theta2_f, z_baja_f, theta3_f, frames=50):
    z_baja_f = np.clip(z_baja_f, 0, Z_TRAVEL_MAX)
    theta1_i = theta2_i = z_i = theta3_i = 0
    
    t1_vals = np.linspace(theta1_i, theta1_f, frames)
    t2_vals = np.linspace(theta2_i, theta2_f, frames)
    z_vals = np.linspace(z_i, z_baja_f, frames)
    t3_vals = np.linspace(theta3_i, theta3_f, frames)
    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    lim = 1200
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(0, 1200)
    
    def update(i):
        ax.cla()
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_zlim(0, 1200)
        ax.set_xlabel('X (mm)')
        ax.set_ylabel('Y (mm)')
        ax.set_zlabel('Z (mm)')
        ax.view_init(elev=25, azim=45)
        
        p_base, p_eje, p1, p2, p3_top, p3_bottom, cx, cy, cz, px, py, pz = fkine_dh(
            t1_vals[i], t2_vals[i], z_vals[i], t3_vals[i]
        )
        
        dibujar_robot(ax, p_base, p_eje, p1, p2, p3_top, p3_bottom, cx, cy, cz, px, py, pz)
        return []
    
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=20, blit=False, repeat=False)
    plt.show()

# ------------------ Programa principal ------------------
if __name__ == "__main__":
    print("Animación Robot SCARA i4-850H")
    theta1 = float(input("Introduce θ1 (brazo 1, grados): "))
    theta2 = float(input("Introduce θ2 (brazo 2, grados): "))
    z_baja = float(input(f"Introduce desplazamiento vertical hacia abajo (mm, 0–{Z_TRAVEL_MAX}): "))
    theta3 = float(input("Introduce θ3 (rotación platillo, grados): "))
    animar_robot(theta1, theta2, z_baja, theta3)
