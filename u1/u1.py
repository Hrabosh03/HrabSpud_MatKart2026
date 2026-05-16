from math import *
from uvtosd import*

def WGSToJTSK (phi_WGS, la_WGS, point_name):
    #WGS84 parameters
    a_WGS = 6378137.00
    b_WGS = 6356752.3142
    
    e2_WGS = (a_WGS*a_WGS - b_WGS*b_WGS)/(a_WGS*a_WGS)
    W_WGS = sqrt(1-e2_WGS*(sin(phi_WGS))**2)
    N_WGS = a_WGS/W_WGS
    
    #XYZ coordinates, WGS 84
    X_WGS = N_WGS * (cos(phi_WGS) * cos(la_WGS))
    Y_WGS = N_WGS * (cos(phi_WGS) * sin(la_WGS))
    Z_WGS = N_WGS * (1 - e2_WGS) * sin(phi_WGS)
    
    #Helmert transformation, parameters
    om_x = 4.9984 / 3600 * pi /180 
    om_y = 1.5867 /3600 * pi / 180
    om_z = 5.2611 /3600 * pi / 180
    m = 1 - 3.5623e-06
    dlt_x = -570.8285
    dlt_y = -85.6769
    dlt_z = -462.8420
    
    #Helmert transformation, Bessel ellipsoid
    X_Bes = m * (X_WGS + Y_WGS * om_z - om_y * Z_WGS) + dlt_x
    Y_Bes = m * (-om_z * X_WGS + Y_WGS + om_x * Z_WGS) + dlt_y
    Z_Bes = m * (om_y * X_WGS - om_x * Y_WGS + Z_WGS) + dlt_z
    
    #Bessel parameters
    a_Bes = 6377397.155
    b_Bes = 6356078.963
    e2_Bes = (a_Bes*a_Bes - b_Bes*b_Bes)/(a_Bes*a_Bes)
   
    #Phi, lam, Bessel
    la_Bes = atan2(Y_Bes,X_Bes)
    tan_phi_Bes = Z_Bes / ((1 - e2_Bes) * sqrt(X_Bes**2 + Y_Bes**2))
    phi_Bes = atan(tan_phi_Bes)
    
    #Shift to Feerro
    la_Ferro = la_Bes + (17 + 2/3) * pi / 180
    
    #Gauss conformal projection, parameters
    phi0 = 49.5 * pi / 180
    alpha = sqrt (1 + e2_Bes * (cos(phi0))**4 / (1 - e2_Bes))
    u0 = asin(sin(phi0)/alpha)
    
    kn = (tan(phi0/2+pi/4)**alpha*((1-sqrt(e2_Bes)*sin(phi0))/(1+sqrt(e2_Bes)*sin(phi0)))**(alpha*sqrt(e2_Bes)/2))
    kd = tan(u0/2+pi/4)
    k = kn / kd
    
    R = (a_Bes*sqrt(1-e2_Bes))/(1-e2_Bes*(sin(phi0)**2))
 
    #Gauss conformal projection
    u = 2*(atan(1/k*(tan(phi_Bes/2+pi/4)*((1-sqrt(e2_Bes)*sin(phi_Bes))/(1+sqrt(e2_Bes)*sin(phi_Bes)))**(sqrt(e2_Bes)/2))**alpha))-pi/2
    v = alpha*la_Ferro
    
    #Cartographic pole
    uk = (59+(42/60)+(42.6969/3600))*(pi/180)
    vk = (42+(31/60)+(31.41725/3600))*(pi/180)
    
    #Conversion (u, v) -> (s, d)
    s, d = uvTosd(u, v, uk, vk)
    
    #LCC
    s0 = 78.5 * pi/180
    rho0 = R*1/tan(s0)*0.9999
    c = sin(s0)
    
    rho = rho0*((tan(s0/2+pi/4))/(tan(s/2+pi/4)))**c
    eps = c * d
    
    # (rho, eps) -> (y, x)
    y_jtsk = rho*sin(eps)
    x_jtsk = rho*cos(eps)
    
    #print(y_jtsk, x_jtsk)
 
    #Length distortion (m-1)
    N_Bes = a_Bes / sqrt(1 - e2_Bes * sin(phi_Bes)**2)
    
    m_1 = (R * cos(u)) / (N_Bes * cos(phi_Bes)) 
    m_2 = (rho * c) / (R * cos(s))              
    
    m_total = m_1 * m_2
    distortion = m_total - 1

    #Meridian convergence
    dv = vk - v
    C_1 = asin((cos(uk) * sin(dv)) / cos(s))    
    C_2 = eps                                   
    
    meridian_conv = C_1 - C_2                   
    meridian_conv_deg = meridian_conv * 180/pi  

    
    print(point_name)
    print(f"Y (JTSK): {y_jtsk:.2f} m")  
    print(f"X (JTSK): {x_jtsk:.2f} m")  
    print(f"Lengh distortion (m-1): {distortion:.6e}")
    print(f"Meridian convergence: {meridian_conv_deg:.4f}°\n")
    
    return y_jtsk, x_jtsk, distortion, meridian_conv


# Point P1
phi_P1 = 50.03060 * pi/180
la_P1 = 14.51013 * pi/180
WGSToJTSK(phi_P1, la_P1, point_name="Point P1")

# Point P2
phi_P2 = 50.06889 * pi/180
la_P2 = 14.42449 * pi/180
WGSToJTSK(phi_P2, la_P2, point_name="Point P2")
