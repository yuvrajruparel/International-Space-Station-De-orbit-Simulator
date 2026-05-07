# assigned to yiannis

import numpy as np
from constants import *    
from shared_funcs import *
from plot import plot_simple

# compute burn time from rocket constants
# burn time = fuel mass / mass flow rate
# fuel mass = M_0_LV - M_0_LV/MASS_RATIO_LV
# burn_time = (M_0_LV - M_0_LV / MASS_RATIO_LV) / M_DOT_E_LV
def current_mass(t, burn_time):
    # rocket mass
    fuel_burned = M_DOT_E_LV * min(t, burn_time)
    return M_0_LV - fuel_burned

def thrust_accel(t, vel, pos, burn_time):
    # no thrust after burn time ends
    if t > burn_time:
        return np.array([0.0, 0.0])

    # thrust = mass flow rate * g * specific impulse
    LV_THRUST = M_DOT_E_LV * g_0 * I_SP_LV
    v = np.linalg.norm(vel)

    # if velocity is very small
    if v < 1e-6:
        r = np.linalg.norm(pos)
        dir_vec = pos / r if r != 0 else np.array([0.0, 1.0])
    else:
        dir_vec = vel / v

    thrust_vec = LV_THRUST * dir_vec
    return thrust_vec / current_mass(t, burn_time) # acceleration

def lv_drag_accel(vel, pos, mass):

    v = np.linalg.norm(vel)
    if v == 0:
        return np.array([0.0, 0.0])

    # altitude = distance - radius of Earth
    r = np.linalg.norm(pos)
    h = r - R_EARTH

    # air density at height h
    rho = RHO_0 * np.exp(-h / H_0)

    # drag magnitude = 0.5 * density * drag coefficient * CSA * vsqrd
    drag_mag = 0.5 * rho * C_D_LV * AREA_LV * v**2
    drag_vec = -drag_mag * (vel / v)

    return drag_vec / mass

# total acceleration = gravity + drag + thrust
def total_accel(pos, vel, t, burn_time):
    mass = current_mass(t, burn_time)
    return gravity_accel(pos) + lv_drag_accel(vel, pos, mass) + thrust_accel(t, vel, pos, burn_time)

def rocket_trajectory(init_pos, init_vel, sim_time, dt, burn_time):

    def total_accel(pos, vel, t):
        mass = current_mass(t, burn_time)
        return ( gravity_accel(pos) + lv_drag_accel(vel, pos, mass) + thrust_accel(t, vel, pos, burn_time) )

    # number of steps 
    N = int(np.ceil(sim_time / dt)) + 1
    t = np.arange(N) * dt

    pos = np.zeros((2, N))
    vel = np.zeros((2, N))

    pos[:, 0] = init_pos
    vel[:, 0] = init_vel

    for i in range(N - 1):
        def accel_fn(p, v):
            return total_accel(p, v, t[i])
        pos[:, i+1], vel[:, i+1] = rk(accel_fn, pos[:, i], vel[:, i], dt)

    return t, pos, vel

def extract_altitude_from_pos(pos):
    r = np.sqrt(pos[0]**2 + pos[1]**2)
    return r - R_EARTH

def find_minimum_fuel_percentage(target_altitude=400_000, dt=0.5):

    low, high = 0.0, 1.0
    tolerance = 0.001   # 0.1%

    while high - low > tolerance:
        mid = (low + high) / 2 

        # compute burn time for this fuel %
        m_i = M_0_LV
        effective_mass_ratio = 1 + (MASS_RATIO_LV - 1) * mid # interpollation formula
        m_f = m_i / effective_mass_ratio
        t_burn = (m_i - m_f) / M_DOT_E_LV # initial - final / flowrate

        t, pos, vel = rocket_trajectory(
            np.array([R_EARTH, 0.0]),
            np.array([0.0, 0.0]),
            8 * t_burn,
            dt,
            t_burn
        )

        altitude = extract_altitude_from_pos(pos)
        max_altitude = np.max(altitude)

        if max_altitude >= target_altitude:
            high = mid
        else:
            low = mid

    return high # since high is the % that succeeds

def main():
    dt = 0.1
    target_altitude = 400_000   # 400 km

    # find minimum fuel percentage
    min_fuel_pct = find_minimum_fuel_percentage(target_altitude, dt)

    init_pos = np.array([R_EARTH, 0.0])
    init_vel = np.array([0.0, 0.0])

    # compute burn time for the minimum fuel percentage
    m_i = M_0_LV
    effective_mass_ratio = 1 + (MASS_RATIO_LV - 1) * min_fuel_pct
    m_f = m_i / effective_mass_ratio # final mass
    t_burn_min = (m_i - m_f) / M_DOT_E_LV 

    # run for 8*t_burn_min
    sim_time = 8 * t_burn_min
    t, pos, vel = rocket_trajectory(init_pos, init_vel, sim_time, dt, t_burn_min)

    altitude_m = extract_altitude_from_pos(pos)
    
    # default to end if never reaches
    for i in range(len(altitude_m)):
        if altitude_m[i] >= target_altitude:
            idx = i
            break  
    
    t = t[: idx+1]
    pos = pos[:, : idx+1]
    vel = vel[:, : idx+1]
    altitude = altitude_m[: idx+1] / 1000   # km

    print("Launch Vehicle Summary")
    print(f"Max altitude: {np.max(altitude):.2f} km")
    print(f"Final altitude: {altitude[-1]:.2f} km")
    print(f"Final velocity: {np.linalg.norm(vel[:, -1]):.1f} m/s")
    print(f"Minimum fuel percentage to exceed 400 km: {min_fuel_pct*100:.2f}%")

    capped_alt = np.clip(altitude, 0, 400)
    plot_simple(t, capped_alt)

if __name__ == "__main__":
    main()
