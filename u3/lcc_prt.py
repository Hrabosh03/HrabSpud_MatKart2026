from math import *
import numpy as np
import matplotlib.pyplot as plt
import graticule as gr
# Optimal LCC projection
R = 1

#Pole
uk = 39.366732414201 * pi/180
vk = -0.968843929589 * pi/180 

#Outer parallel point
u1 = 38.780712127563 *pi/180
v1 = -9.500531196058 *pi/180

#Inner parallel point
u2 = 40.012508391749 *pi/180
v2 = -6.863883971768 *pi/180

#Transformation to the oblique aspect
s1 = asin(sin(u1) * sin(uk) + cos(u1) * cos(uk) * cos(vk-v1))
s2 = asin(sin(u2) * sin(uk) + cos(u2) * cos(uk) * cos(vk-v2))

#Constant c of the conic projection
cn = log10(cos(s1)) - log10(cos(s2))
cd = log10(tan(s2/2+pi/4))-log10(tan(s1/2+pi/4))
c = cn / cd

#Compute s0
s0 = asin(c)

#Compute rho0: radius of the parallel (u = u0)
rho0_n = 2*R*cos(s0)*cos(s1)*(tan(s1/2+pi/4))**c
rho0_d = c*(cos(s0)*(tan(s0/2+pi/4))**c+cos(s1)*(tan(s1/2+pi/4))**c)
rho0 = rho0_n/rho0_d

#Compute rho1: radius of the north parallel (u = u1)
rho1 = rho0*((tan(s0/2+pi/4))/(tan(s1/2+pi/4)))**c

#Compute rho2: radius of the south parallel (u = u2)
rho2 = rho0*((tan(s0/2+pi/4))/(tan(s2/2+pi/4)))**c

#Scales
m1 = (c * rho1)/(R * cos(s1))
m2 = (c * rho2)/(R * cos(s2))
m0 = (c * rho0)/(R * cos(s0))

ny1 = (m1 -1) * 1000
ny2 = (m2 -1) * 1000
ny0 = (m0 - 1) * 1000

print(ny1, ny2, ny0)

#UV to SD
def uv_to_sd_lcc(u, v, uk, vk):    
    s, d = gr.uv_to_sd(u, v, uk, vk)
    d = np.mod(d, 2 * pi)
    return s, d

#Rotate
def rotate(X, Y, theta):
    return X * cos(theta) - Y * sin(theta), X * sin(theta) + Y * cos(theta)

#Rotation calculation
u_c, v_c = 39.5 * pi/180, -8.0 * pi/180 
u_n, v_n = 40.5 * pi/180, -8.0 * pi/180 

sc, dc = uv_to_sd_lcc(u_c, v_c, uk, vk)
sn, dn = uv_to_sd_lcc(u_n, v_n, uk, vk)

Xc, Yc, _ = gr.lcc(sc, dc, s1, s2)
Xn, Yn, _ = gr.lcc(sn, dn, s1, s2)

theta = pi/2 - atan2(Yn - Yc, Xn - Xc)


plt.figure(figsize=(9, 9))

Du, dv = 1.0, 0.1 
Dv, du = 1.0, 0.1 
umin, umax = 36.0, 43.0  
vmin, vmax = -10.5, -5.5  

#Meridians
for v in np.arange(vmin, vmax + Dv, Dv):
    um = np.arange(umin, umax + du, du) * pi/180
    vm = np.full(len(um), v) * pi/180
    sm, dm = uv_to_sd_lcc(um, vm, uk, vk)
    xm, ym, _ = gr.lcc(sm, dm, s1, s2)
    xm, ym = rotate(xm, ym, theta)
    plt.plot(xm, ym, color='black', linewidth=0.5, zorder=1)

#Parallels
for u in np.arange(umin, umax + Du, Du):
    vp = np.arange(vmin, vmax + dv, dv) * pi/180
    up = np.full(len(vp), u) * pi/180
    sp, dp = uv_to_sd_lcc(up, vp, uk, vk)
    xp, yp, _ = gr.lcc(sp, dp, s1, s2)
    xp, yp = rotate(xp, yp, theta)
    plt.plot(xp, yp, color='black', linewidth=0.5, zorder=1)

#Distorton isolines
u_grid = np.linspace(umin * pi/180, umax * pi/180, 200)
v_grid = np.linspace(vmin * pi/180, vmax * pi/180, 200)
U, V = np.meshgrid(u_grid, v_grid)
S, D = uv_to_sd_lcc(U, V, uk, vk)
X_grid, Y_grid, NY_grid = gr.lcc(S, D, s1, s2)
X_grid, Y_grid = rotate(X_grid, Y_grid, theta)

levels = np.arange(-0.1, 0.1, 0.025)
contours = plt.contour(X_grid, Y_grid, NY_grid, levels=levels, colors='red', linewidths=1.2, zorder=3)
plt.clabel(contours, inline=True, fontsize=8, fmt='%1.3f')

#State border
try:
    stat_data = np.loadtxt('prt_vertices.txt', delimiter='\t') 
    stat_v = stat_data[:, 0] * pi/180
    stat_u = stat_data[:, 1] * pi/180
    
    stat_s, stat_d = uv_to_sd_lcc(stat_u, stat_v, uk, vk)
    stat_X, stat_Y, _ = gr.lcc(stat_s, stat_d, s1, s2)
    stat_X, stat_Y = rotate(stat_X, stat_Y, theta)
    
    plt.plot(stat_X, stat_Y, color='blue', linewidth=1.5, zorder=2)
except FileNotFoundError:
    print("file not found")

plt.title("Lambert conformal conic projection - Portugal")
plt.axis('equal') 
plt.show()