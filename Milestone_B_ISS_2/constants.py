import math


# Constants
G = 6.67e-11       # N*m^2/kg^2
M_EARTH = 5.972e24 # kg
R_EARTH = 6378e3   # m
g_0 = 9.81         # accel gravity (m/s^2)

# Constants for atmospheric density model
RHO_LEO = 3.8e-12  # mean level air density at LEO 
                   # from MSISe-90 Atmosphere Model (kg/m^3)
RHO_0 = 1.225      # air density at sea level (kg/m^3)
H_0 = 7500.        # scale height (m)

# ISS parameters
C_D_ISS = 2.07  # ESA
M_ISS = 450000  # kg
AREA_ISS = 1000 # m^2 (between 700 and 2300 depends on config)
M_TRUSS = 8755 + 15824 + 13971 + 14124 + 14003 + 2*15824 + 1864 + 2*15824 + 1818 + 15824 # kg (https://en.wikipedia.org/wiki/Integrated_Truss_Structure)
C_D_TRUSS = 2.0
AREA_TRUSS = 700

# Deorbit vehicle parameters
M_DV = 30000  # kg
THRUST = 3236 # N

# Launch vehicle parameters
M_0_LV = 1.42e6         # initial mass of rocket (kg)
MASS_RATIO_LV = 19.5    # mass ratio
I_SP_LV = 282.          # specific impulse (s)
M_DOT_E_LV = 8788.      # rocket exhaust mass flow rate (kg/s)
C_D_LV = 1.2            # drag coefficient
AREA_LV = math.pi*(3.7/2)**2*3 # frontal area (m^2)
