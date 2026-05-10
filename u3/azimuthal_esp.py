from math import *
import numpy as np
import matplotlib.pyplot as plt
import graticule as gr

#Optimal azimuthal projection
R = 1

#Pole
uk = 40.933146766254 * pi/180 
vk = -3.174712367813 * pi/180  

#Furthest point
u1 = 43.056805000351 * pi/180  
v1 = -9.299860000039 * pi/180  


#Transformation to the oblique aspect
s_j = asin(sin(u1) * sin(uk) + cos(u1) * cos(uk) * cos(v1 - vk))

#Complement to 90 deg
psi_j = pi/2 - s_j

#Multiplication constant
mu = (2 * (cos(psi_j / 2))**2) / (1 + (cos(psi_j / 2))**2)

#Psi 0
psi_0 = 2 * acos(sqrt(mu))

#Scales
m_pole = (cos(psi_0 / 2))**2
m_edge = m_pole / (cos(psi_j / 2))**2

#Distortions
ny_pole = (m_pole - 1) * 1000 
ny_edge = (m_edge - 1) * 1000

print(ny_pole, ny_edge)

#UV to SD
def uv_to_sd_az(u, v, uk, vk):    
    s, d = gr.uv_to_sd(u, v, uk, vk)
    d = np.mod(d, 2 * pi)
    return s, d

#Rotate coordinates
def rotate(X, Y, theta):
    return X * cos(theta) - Y * sin(theta), X * sin(theta) + Y * cos(theta)

#Rotation calculation
u_c, v_c = uk, vk 
u_n, v_n = uk + 1.0 * pi/180, vk 

sc, dc = uv_to_sd_az(u_c, v_c, uk, vk)
sn, dn = uv_to_sd_az(u_n, v_n, uk, vk)

Xc, Yc, _ = gr.azimuthal(sc, dc, psi_0, R)
Xn, Yn, _ = gr.azimuthal(sn, dn, psi_0, R)

theta = pi/2 - atan2(Yn - Yc, Xn - Xc)

plt.figure(figsize=(9, 9))

#Bounding box and grid spacing
Du, dv = 1.0, 0.1 
Dv, du = 1.0, 0.1 
umin, umax = 35.0, 44.0  
vmin, vmax = -10.0, 5.0  

#Meridians
for v in np.arange(vmin, vmax + Dv, Dv):
    um = np.arange(umin, umax + du, du) * pi/180
    vm = np.full(len(um), v) * pi/180
    sm, dm = uv_to_sd_az(um, vm, uk, vk)
    xm, ym, _ = gr.azimuthal(sm, dm, psi_0, R)
    xm, ym = rotate(xm, ym, theta)
    plt.plot(xm, ym, color='black', linewidth=0.5, zorder=1)

#Parallels
for u in np.arange(umin, umax + Du, Du):
    vp = np.arange(vmin, vmax + dv, dv) * pi/180
    up = np.full(len(vp), u) * pi/180
    sp, dp = uv_to_sd_az(up, vp, uk, vk)
    xp, yp, _ = gr.azimuthal(sp, dp, psi_0, R)
    xp, yp = rotate(xp, yp, theta)
    plt.plot(xp, yp, color='black', linewidth=0.5, zorder=1)

#Distortion isolines
u_grid = np.linspace(umin * pi/180, umax * pi/180, 200)
v_grid = np.linspace(vmin * pi/180, vmax * pi/180, 200)
U, V = np.meshgrid(u_grid, v_grid)
S, D = uv_to_sd_az(U, V, uk, vk)

#Optimal distortion
X_grid, Y_grid, NY_grid = gr.azimuthal(S, D, psi_0, R)
X_grid, Y_grid = rotate(X_grid, Y_grid, theta)

levels = np.arange(-1.2, 1.2, 0.15)
contours = plt.contour(X_grid, Y_grid, NY_grid, levels=levels, colors='red', linewidths=1.2, zorder=3)
plt.clabel(contours, inline=True, fontsize=10, fmt='%1.2f')

#State border
try:
    stat_data = np.loadtxt('esp_vertices.txt', delimiter='\t') 
    stat_v = stat_data[:, 0] * pi/180
    stat_u = stat_data[:, 1] * pi/180
    
    stat_s, stat_d = uv_to_sd_az(stat_u, stat_v, uk, vk)
    stat_X, stat_Y, _ = gr.azimuthal(stat_s, stat_d, psi_0, R)
    stat_X, stat_Y = rotate(stat_X, stat_Y, theta)
    
    plt.plot(stat_X, stat_Y, color='blue', linewidth=1.5, zorder=2)
except FileNotFoundError:
    print("file not found")

plt.title("Azimuthal conformal projection - Spain")
plt.axis('equal') 
plt.show()

