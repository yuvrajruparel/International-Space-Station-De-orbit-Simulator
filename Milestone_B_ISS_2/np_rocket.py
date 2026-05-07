# launch vehicle yiannis

import numpy as np
import math
from constants import *
from plot import plot_simple

#earth constants
G = 6.674e-11        # gravitational constant
M_E = 5.972e24       # mass of Earth 
R_E = 6.371e6        # radius of Earth


def burn_time_and_final_mass():
    # compute burn time and final mass
    m_i = M_0_LV
    m_f = m_i / MASS_RATIO_LV
    t_burn = (m_i - m_f) / M_DOT_E_LV
    return t_burn, m_f


def air_density(h):
    # exponential air density model
    if h < 0:
        h = 0
    return RHO_0 * math.exp(-h / H_0)


def gravity_mag(h):
    # gravitational acceleration at altitude h
    return G * M_E / (R_E + h) ** 2


def rocket_trajectory(dt=0.1, target_altitude=400_000, fuel_percentage=1.0):
    # scale mass ratio based on fuel percentage
    effective_mass_ratio = 1 + (MASS_RATIO_LV - 1) * fuel_percentage
    m_i = M_0_LV
    m_f = m_i / effective_mass_ratio
    t_burn = (m_i - m_f) / M_DOT_E_LV
    total_time = 8 * t_burn
    T = M_DOT_E_LV * I_SP_LV * g_0

    n_steps = int(total_time / dt)
    t = np.zeros(n_steps)
    y = np.zeros(n_steps)
    v = np.zeros(n_steps)

    for i in range(1, n_steps):
        rho = air_density(y[i - 1])
        g = gravity_mag(y[i - 1])
        Fd = 0.5 * rho * C_D_LV * AREA_LV * v[i - 1] * abs(v[i - 1])

        if t[i - 1] <= t_burn:
            Ft = T
            m = M_0_LV - M_DOT_E_LV * t[i - 1]
        else:
            Ft = 0
            m = M_0_LV - M_DOT_E_LV * t_burn

        a = (Ft - Fd - m * g) / m
        v[i] = v[i - 1] + a * dt
        y[i] = y[i - 1] + v[i - 1] * dt
        t[i] = t[i - 1] + dt

        if y[i] < 0 or y[i] >= target_altitude:
            t = t[:i + 1]
            y = y[:i + 1]
            v = v[:i + 1]
            break

    r_final = np.array([0, y[-1]])
    v_final = np.array([0, v[-1]])
    return t, y, v, r_final, v_final


def find_minimum_fuel_percentage(target_altitude=400_000, dt=0.1):

    low, high = 0.0, 1.0
    tolerance = 0.001  # 0.1% tolerance
    
    while high - low > tolerance:
        mid = (low + high) / 2
        t, y, v, _, _ = rocket_trajectory(dt, target_altitude, mid)
        max_altitude = np.max(y)
        
        if max_altitude >= target_altitude:
            high = mid  # if it can achieve target, try lower fuel
        else:
            low = mid   # if it cannot achieve target, need more fuel
    
    return high


def main():
    dt = 0.1
    target_altitude = 400_000
    
    # find minimum fuel percentage
    min_fuel_pct = find_minimum_fuel_percentage(target_altitude, dt)
    
    t, y, v, r_final, v_final = rocket_trajectory(dt, target_altitude, fuel_percentage=1.0)

    print("Launch Vehicle Summary")
    print(f"Max altitude: {np.max(y)/1000:.2f} km")
    print(f"Final altitude: {y[-1]/1000:.2f} km")
    print(f"Final velocity: {v[-1]:.1f} m/s")
    print(f"Minimum fuel percentage to exceed {target_altitude/1000:.0f} km: {min_fuel_pct*100:.2f}%")

    plot_simple(t, y / 1000)  # altitude in km



if __name__ == "__main__":
    main()
