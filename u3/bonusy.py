import numpy as np
from math import *
from scipy.optimize import minimize

#1
def pole_merc(borders):
    #Load data
    try:
        data = np.loadtxt(borders, delimiter='\t')
    except FileNotFoundError:
        return None, None
        
    v = data[:, 0] * pi/180  
    u = data[:, 1] * pi/180  
    
    #uv to Cartesian coordinates
    x = np.cos(u) * np.cos(v)
    y = np.cos(u) * np.sin(v)
    z = np.sin(u)

    #Coordinates matrix
    A = np.column_stack((x, y, z))

    #Least squares using SVD
    U, S, Vh = np.linalg.svd(A)
    
    # Normal vector (last row of Vh matrix)
    nx, ny, nz = Vh[-1, :]

    #Normal vector to uk,vk
    uk = asin(nz)
    vk = atan2(ny, nx)

    #Pole on northern hemisphere 
    if uk < 0:
        uk = -uk
        vk = vk + pi if vk <= 0 else vk - pi

    return uk * 180/pi, vk * 180/pi

uk_esp, vk_esp = pole_merc('esp_vertices.txt')
print('Kartografický pól válcové zobr.')
if uk_esp:
    print(f"Španělsko:   uk = {uk_esp:.6f}°, vk = {vk_esp:.6f}°")

uk_prt, vk_prt = pole_merc('prt_vertices.txt')
if uk_prt:
    print(f"Portugalsko: uk = {uk_prt:.6f}°, vk = {vk_prt:.6f}°")
    
    
#2
def exact_s0(borders, uk_deg, vk_deg):
     #Load data
    try:
        data = np.loadtxt(borders, delimiter='\t')
    except FileNotFoundError:
        return None, None
        
    v = data[:, 0] * pi/180  
    u = data[:, 1] * pi/180  
    
    uk = uk_deg * pi/180
    vk = vk_deg * pi/180

    #Vector calculation of the cartographic latitude for all points on the boundary
    s_all = np.arcsin(np.sin(u) * np.sin(uk) + np.cos(u) * np.cos(uk) * np.cos(v - vk))

    #Furthest point from equator
    s_max = max(abs(s_all))

    #Undistorted parallel s0
    s0 = np.arccos(2 * np.cos(s_max) / (1 + np.cos(s_max)))

    return s_max * 180/pi, s0 * 180/pi

print('Dotyková rovnoběžka')
if uk_esp:
    s_max_esp, s0_esp = exact_s0('esp_vertices.txt', uk_esp, vk_esp)
    print(f"Španělsko:   s_max = {s_max_esp:.6f}°, s0 = {s0_esp:.6f}°")

if uk_prt:
    s_max_prt, s0_prt = exact_s0('prt_vertices.txt', uk_prt, vk_prt)
    print(f"Portugalsko: s_max = {s_max_prt:.6f}°, s0 = {s0_prt:.6f}°")
    
def pole_az(borders):
    try:
        data = np.loadtxt(borders, delimiter='\t')
    except FileNotFoundError:
        return None, None
        
    v = data[:, 0] * pi/180   
    u = data[:, 1] * pi/180  
    
    #max distance from pole
    def max_dist(pole):
        uk, vk = pole
        #Spherical distance
        dist = np.arccos(np.sin(u)*np.sin(uk) + np.cos(u)*np.cos(uk)*np.cos(v - vk))
        #max dist
        return max(dist)

    #State center
    center = [np.mean(u), np.mean(v)]
    
    #Optimalization
    pole_res = minimize(max_dist, center, method='Nelder-Mead')
    
    #Optimized coordinates
    uk_opt, vk_opt = pole_res.x
    
    return uk_opt * 180/pi, vk_opt * 180/pi


uk_az_esp, vk_az_esp = pole_az('esp_vertices.txt')
print('Kartografický pól azimutální zobr.')
if uk_az_esp:
    print(f"Španělsko:   uk = {uk_az_esp:.6f}°, vk = {vk_az_esp:.6f}°")

uk_az_prt, vk_az_prt = pole_az('prt_vertices.txt')
if uk_az_prt:
    print(f"Portugalsko: uk = {uk_az_prt:.6f}°, vk = {vk_az_prt:.6f}°")
    

