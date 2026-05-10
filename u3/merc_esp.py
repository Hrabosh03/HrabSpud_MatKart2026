from math import *
import numpy as np
import matplotlib.pyplot as plt
import graticule as gr

#Optimal Mercator projection

#Points on the quator
u1 = 43.488772995632*pi/180
v1 = -2.366895041672*pi/180
u2 = 36.124051349382*pi/180
v2 = -6.632986485459*pi/180

#Westernmost point
u3 = 43.056805000498*pi/180
v3 = -9.299860000461*pi/180

#Easternmost point
u4 = 41.861805001031*pi/180
v4 = 3.187915999895*pi/180
 
#Pole
vk = atan2(tan(u1)*cos(v2)-tan(u2)*cos(v1), tan(u2)*sin(v1)-tan(u1)*sin(v2))
uk = atan(-1/tan(u2)*cos(vk-v2))

#Transformation to the oblique aspect
s1 = asin(sin(u1) * sin(uk) + cos(u1) * cos(uk) * cos(vk-v1))
s2 = asin(sin(u2) * sin(uk) + cos(u2) * cos(uk) * cos(vk-v2))
s3 = asin(sin(u3) * sin(uk) + cos(u3) * cos(uk) * cos(vk-v3))
s4 = asin(sin(u4) * sin(uk) + cos(u4) * cos(uk) * cos(vk-v4))

#True parallel
s0 = acos (2*cos(s3)/(1+cos(s3)))

#Scales
m1 = cos(s0)/cos(s1)
m2 = cos(s0)/cos(s2)
m3 = cos(s0)/cos(s3)
m4 = cos(s0)/cos(s4)

#Distortions
ny1 = (m1 -1) *1000
ny2 = (m2 -1) *1000
ny3 = (m3 -1) *1000
ny4 = (m4 -1) *1000

print(ny1, ny2, ny3, ny4)

R = 1
# UV to SD 
u_c, v_c = 40.933 * pi/180, -3.174 * pi/180
_, dc = gr.uv_to_sd(u_c, v_c, uk, vk)

def get_continuous_sd(u, v):
    s, d = gr.uv_to_sd(u, v, uk, vk)
    d = d - 2 * pi * np.round((d - dc) / (2 * pi))
    return s, d

#Rotate coordinates
def rotate(X, Y, theta):
    return X * cos(theta) - Y * sin(theta), X * sin(theta) + Y * cos(theta)

#Rotation calculation
u_n, v_n = u_c + 1.0 * pi/180, v_c 

sc, dc_cont = get_continuous_sd(u_c, v_c)
sn, dn_cont = get_continuous_sd(u_n, v_n)

Xc, Yc, _ = gr.mercator(sc, dc_cont, s0, R)
Xn, Yn, _ = gr.mercator(sn, dn_cont, s0, R)

theta = pi/2 - atan2(Yn - Yc, Xn - Xc)

plt.figure(figsize=(10, 8))

#Bounding box and grid spacing
Du, dv = 1.0, 0.1 
Dv, du = 1.0, 0.1 
umin, umax = 35.0, 44.0  
vmin, vmax = -10.0, 5.0  

#Meridians
for v in np.arange(vmin, vmax + Dv, Dv):
    um = np.arange(umin, umax + du, du) * pi/180
    vm = np.full(len(um), v) * pi/180
    sm, dm = get_continuous_sd(um, vm)
    xm, ym, _ = gr.mercator(sm, dm, s0, R)
    xm, ym = rotate(xm, ym, theta)
    plt.plot(xm, ym, color='black', linewidth=0.5, zorder=1)

#Parallels
for u in np.arange(umin, umax + Du, Du):
    vp = np.arange(vmin, vmax + dv, dv) * pi/180
    up = np.full(len(vp), u) * pi/180
    sp, dp = get_continuous_sd(up, vp)
    xp, yp, _ = gr.mercator(sp, dp, s0, R)
    xp, yp = rotate(xp, yp, theta)
    plt.plot(xp, yp, color='black', linewidth=0.5, zorder=1)

#Distortion isolines
u_grid = np.linspace(umin * pi/180, umax * pi/180, 200)
v_grid = np.linspace(vmin * pi/180, vmax * pi/180, 200)
U, V = np.meshgrid(u_grid, v_grid)
S, D = get_continuous_sd(U, V)

X_grid, Y_grid, NY_grid = gr.mercator(S, D, s0, R)
X_grid, Y_grid = rotate(X_grid, Y_grid, theta)


levels = np.arange(-1.5, 1.5, 0.25)
contours = plt.contour(X_grid, Y_grid, NY_grid, levels=levels, colors='red', linewidths=1.2, zorder=3)
plt.clabel(contours, inline=True, fontsize=10, fmt='%1.2f')

#State border
try:
    stat_data = np.loadtxt('esp_vertices.txt', delimiter='\t') 
    stat_v = stat_data[:, 0] * pi/180
    stat_u = stat_data[:, 1] * pi/180
    
    stat_s, stat_d = get_continuous_sd(stat_u, stat_v)
    stat_X, stat_Y, _ = gr.mercator(stat_s, stat_d, s0, R)
    stat_X, stat_Y = rotate(stat_X, stat_Y, theta)
    
    plt.plot(stat_X, stat_Y, color='blue', linewidth=1.5, zorder=2)
except FileNotFoundError:
    print("File not found.")

plt.title("Mercator conformal projection - Spain")
plt.axis('equal') 
plt.show()