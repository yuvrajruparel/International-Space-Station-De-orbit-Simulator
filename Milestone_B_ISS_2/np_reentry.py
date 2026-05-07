# Assigned to Yuvraj

import numpy as np
import matplotlib.pyplot as plt
from constants import *
from plot import plot_position_earth

def gravity_force(mass, x, y):
    """
    Simulates gravity force
    """
    r = np.sqrt(x**2 + y**2)                            # distance from Earth's center
    F_x = -G * M_EARTH * mass * x / r**3                # gravity force in x-direction
    F_y = -G * M_EARTH * mass * y / r**3                # gravity force in y-direction
    return F_x, F_y

def atmospheric_density(altitude):
    """
    Calculates atmospheric density with exponential scale
    """
    altitude = np.maximum(altitude, 0.0)                # prevent negative altitudes
    return RHO_0 * np.exp(-altitude / H_0)

def drag_accel(vel, pos):
    """
    Finds acceleration due to drag
    """
    v = np.sqrt(vel[0]**2 + vel[1]**2) # velocity magnitude
    if v == 0:
        return np.array([0.0, 0.0])
    r = np.sqrt(pos[0]**2 + pos[1]**2)
    h = r - R_EARTH
    rho = RHO_0 * np.exp(-h / 7000.0)
    drag_mag = 0.5 * rho * C_D_ISS * AREA_ISS * v**2 # drag magnitude
    drag_vec = -drag_mag * (vel / v)
    return drag_vec / (M_ISS + M_DV)

def simulate_reentry(dt, init_pos, init_vel, mass):
    """
    Simulation of reentry using numpy arrays.
    Takes dt, init_pos, init_vel, mass
    Returns t_arr, pos, vel
    """
    x, y = init_pos[0], init_pos[1] # position (m)
    vx, vy = init_vel[0], init_vel[1] # velocity (m/s)
    t = 0.0

    x_list, y_list = [x], [y]
    vx_list, vy_list = [vx], [vy]
    t_list = [t]

    for _ in range(5400+1): # simulate ~90 minutes
        r = np.sqrt(x**2 + y**2)
        h = r - R_EARTH
        if h <= 0:
            break # stop when hitting Earth

        F_x_grav, F_y_grav = gravity_force(mass, x, y)
        vel_vec = np.array([vx, vy])
        pos_vec = np.array([x, y])
        a_drag = drag_accel(vel_vec, pos_vec)

        a_x = (F_x_grav / mass) + a_drag[0]
        a_y = (F_y_grav / mass) + a_drag[1]

        vx = vx + a_x * dt
        vy = vy + a_y * dt
        x = x + vx * dt
        y = y + vy * dt
        t += dt

        x_list.append(x)
        y_list.append(y)
        vx_list.append(vx)
        vy_list.append(vy)
        t_list.append(t)

    x_arr = np.array(x_list)
    y_arr = np.array(y_list)
    vx_arr = np.array(vx_list)
    vy_arr = np.array(vy_list)
    t_arr = np.array(t_list)

    pos = np.vstack((x_list, y_list))
    vel = np.vstack((vx_list, vy_list))

    return t_arr, pos, vel

def main():
    dt = 1.0 # timestep (s)
    h0 = 130000.0 # initial altitude (m)
    v0 = 7800.0 # initial tangential velocity (m/s)
    mass = M_ISS + M_DV # ISS + deorbit vehicle (kg)

    init_pos = np.array([0.0, R_EARTH + h0])
    init_vel = np.array([v0, 0.0])

    t, pos, vel = simulate_reentry(dt, init_pos, init_vel, mass)
    plot_position_earth(pos[0,:],pos[1,:])

    print("Reentry simulation with drag completed successfully.")
    print(f"Position array: ", pos)
    print(f"Velocity array:", vel)
    print(f"Simulation steps: {len(t)}")
    print(f"Final time: {t[-1]:.2f} s")
    print(f"Final altitude: {np.sqrt(pos[0,-1]**2 + pos[1,-1]**2) - R_EARTH:.2f} m")

if __name__ == "__main__":
    main()