from numpy import *
from pyproj import *
from matplotlib.pyplot import *

def project(proj_name, R_z, lat, lon, lat0, lon0):
    # Create new projection given by proj_name
    my_proj =  Proj(proj=proj_name, R=R_z, lat_1 = lat0, lat_0 = lat0, lon_0 = lon0)

    # Project point calculation
    [X,Y] = my_proj(lon, lat)

    #Distortions
    dist = my_proj.get_factors(lon, lat)
    a = dist.tissot_semimajor
    b = dist.tissot_semiminor

    return X, Y, a, b 

def graticule(lat_min, lon_min, lat_max, lon_max, Dlat, Dlon, dlat, dlon, R, lat0, lon0, proj_name):
    #Create graticule of the given map projection
    #Create meridians
    lat_mer = arange(lat_min, lat_max + dlat/2, dlat)
    lon_mer = arange(lon_min, lon_max + Dlon/2, Dlon)
    
    #Create parallels
    lat_par = arange(lat_min, lat_max + Dlat/2, Dlat)
    lon_par = arange(lon_min, lon_max + dlon/2, dlon)

    #Create meshgrid
    lat_merg, lon_merg = meshgrid(lat_mer, lon_mer)
    lon_parg, lat_parg = meshgrid(lon_par, lat_par)
    
    #Project meridians
    mer_proj = project(proj_name, R, lat_merg, lon_merg, lat0, lon0)

    #Project parallels
    par_proj = project(proj_name, R, lat_parg, lon_parg, lat0, lon0)
    
    return mer_proj, par_proj   

#Define projection

#proj_name = "bonne"    # Bonne projection
#proj_name = "sinu"  # Mercator-Sanson (sinusoidal) projection
#proj_name = "eck5"    # Eckert V projection
#proj_name = "wintri"   # Winkel Tripel projection
#proj_name = "hammer"   # Hammer-Aitoff projection
proj_name = "lcc"    # Lambert Conformal Conic projection

R = 6378000
lat0 = 50
lon0 = 15

# Define projection grid
lat_min = 34
lat_max = 72
lon_min = -12
lon_max = 35

Dlat = 5
Dlon = 5
dlat = 0.1 * Dlat
dlon = 0.1 * Dlon
nlat = 100
nlon = 100

#Create intervals
lat = linspace(lat_min, lat_max, nlat)
lon = linspace(lon_min, lon_max, nlon)

#Create meshgrid
latg, long = meshgrid(lat, lon)

#Project meshgrid
X, Y, a, b = project(proj_name, R, latg, long, lat0, lon0)

#Airy local
h2_a = 0.5*((a-1)**2+(b-1)**2)

#Complex local
h2_c = 0.5*(abs(a-1)+abs(b-1)) + a/b - 1

#Airy global
H2_a = mean(h2_a)

#Complex global
H2_c = mean(h2_c)

#Airy weighted global
w = cos(latg * pi / 180)
H2_aw = sum(w*h2_a)/sum(w)

#Complex weighted global
H2_cw = sum(w*h2_c)/sum(w)

print(f"H2_a: {H2_a}, H2_c: {H2_c}") 
print(f"H2_aw: {H2_aw}, H2_cw: {H2_cw}")

#Draw EU countries
continents = loadtxt("EU_data.txt")

#Extract coordinates
latc = continents[:, 0]
lonc = continents[:, 1]

#Project points
Xc, Yc, ac, bc = project(proj_name, R, latc, lonc, lat0, lon0)

Xc[isnan(lonc)] = nan
Yc[isnan(latc)] = nan

#Draw points
plot(Xc, Yc, linewidth=1.5)

#Create meridians and parallels
mer_proj, par_proj = graticule(lat_min, lon_min, lat_max, lon_max, Dlat, Dlon, dlat, dlon, R, lat0, lon0, proj_name)

#Extract coordinates
Xm = mer_proj[0]
Ym = mer_proj[1]

Xp = par_proj[0]
Yp = par_proj[1]

#Plot meridians and parallels
plot(transpose(Xm), transpose(Ym), color='black', linewidth=0.5)
plot(transpose(Xp), transpose(Yp), color='black', linewidth=0.5)

#Variable map scale
S = 100000000
Sv = S/a
dS = arange(80000000, 120000000, 5000000) 

#Draw contours of variable map scale
contours = contour(X, Y, Sv, levels=dS, colors='red', linewidths=1.5)

#Label contours 
clabel(contours, inline=True, fontsize=10, colors='darkred')

gca().set_aspect('equal', adjustable='datalim')
axis('off')
tight_layout()

show()