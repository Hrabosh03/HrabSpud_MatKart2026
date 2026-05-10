import numpy as np

def uv_to_sd(u, v, uk, vk):
    #Transformation of geographic coordinates to oblique aspect
    s = np.arcsin(np.sin(u)*np.sin(uk) + np.cos(u)*np.cos(uk)*np.cos(v - vk))
    num = np.cos(u)*np.sin(v - vk)
    den = np.cos(u)*np.sin(uk)*np.cos(v - vk) - np.sin(u)*np.cos(uk)
    d = np.arctan2(num, den)
    return s, d

def mercator(s, d, s0, R=1.0):
    #Mercator projection (Cylindrical conformal)
    c = R * np.cos(s0)
    X = c * d
    Y = R * np.log(np.tan(s/2 + np.pi/4))
    m = np.cos(s0) / np.cos(s)
    ny = (m - 1) * 1000
    return X, Y, ny

def azimuthal(s, d, psi0, R=1.0):
    #Azimuthal conformal projection (Stereographic)
    psi = np.pi/2 - s
    rho = 2 * R * (np.cos(psi0/2)**2) * np.tan(psi/2)
    X = rho * np.sin(d)
    Y = -rho * np.cos(d)
    m = (np.cos(psi0/2)**2) / (np.cos(psi/2)**2)
    ny = (m - 1) * 1000
    return X, Y, ny

def lcc(s, d, s1, s2, R=1.0):
    #Lambert conformal conic projection (LCC) - Optimized aspect
    #c constant
    c_num = np.log(np.cos(s1)) - np.log(np.cos(s2))
    c_den = np.log(np.tan(s2/2 + np.pi/4)) - np.log(np.tan(s1/2 + np.pi/4))
    c = c_num / c_den
    
    #Latitude of an undistorted parallel
    s0 = np.arcsin(c)
    
    #Auxiliary tangents
    tan_s0_c = np.tan(s0/2 + np.pi/4)**c
    tan_s1_c = np.tan(s1/2 + np.pi/4)**c
    tan_s_c = np.tan(s/2 + np.pi/4)**c
    
    #Optimized rho0 
    rho0_num = 2 * R * np.cos(s0) * np.cos(s1) * tan_s1_c
    rho0_den = c * (np.cos(s0) * tan_s0_c + np.cos(s1) * tan_s1_c)
    rho0 = rho0_num / rho0_den
    
    #rho
    rho = rho0 * (tan_s0_c / tan_s_c)
    
    #Projection equation
    X = rho * np.sin(c * d)
    Y = rho0 - rho * np.cos(c * d)
    
    #Optimized distortion
    m = (rho * c) / (R * np.cos(s))
    ny = (m - 1) * 1000
    
    return X, Y, ny