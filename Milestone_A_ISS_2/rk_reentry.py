# Assigned to Yuvraj

import numpy as np
import matplotlib.pyplot as plt
from constants import *
from plot import plot_position_earth
from shared_funcs import *

def accel(position, velocity, mass):
    """
    Total acceleration = gravity + drag
    """
    total = gravity_accel(position) + drag_accel(velocity, position, mass)
    return total

def truss_drag_accel(vel, pos, mass):
    """
    Computes drag acceleration vector for truss.
    Drag = -0.5 * rho(h) * Cd * A * v^2 * v_hat
    """
    v = np.sqrt(vel[0]**2 + vel[1]**2)
    if v == 0:
        return np.array([0.0, 0.0])

    # altitude = distance - radius of Earth
    r = np.sqrt(pos[0]**2 + pos[1]**2)
    h = r - R_EARTH

    # atmospheric density model
    rho = RHO_0 * np.exp(-h / H_0)

    drag_mag = 0.5 * rho * C_D_TRUSS * AREA_TRUSS * v**2
    drag_vec = -drag_mag * (vel / v)

    return drag_vec / (mass)

def truss_accel(position, velocity, mass):
    """
    Total acceleration = gravity + drag
    """
    total = gravity_accel(position) + truss_drag_accel(velocity, position, mass)
    return total

def simulate_reentry(dt, init_pos, init_vel, mass):
    """
    Simulation of reentry using numpy arrays.
    Takes dt, init_pos, init_vel, mass
    Uses Runge-Kutta method to find new position
    Returns t_arr, pos, vel
    """

    pos = np.array(init_pos)
    vel = np.array(init_vel)
    t = 0.0

    pos_list = [pos.copy()]
    vel_list = [vel.copy()]
    t_list = [t]

    def accel_without_mass(pos, vel):
        return accel(pos, vel, mass)

    while np.linalg.norm(pos) > 100000+R_EARTH:
        pos, vel = rk(accel_without_mass, pos, vel, dt)
        t += dt

        pos_list.append(pos.copy())
        vel_list.append(vel.copy())
        t_list.append(t)

    pos_old = pos 
    horizontal_distance = 0

    def truss_accel_no_mass(pos,vel):
        return truss_accel(pos, vel, M_TRUSS)
    
    while np.linalg.norm(pos) > R_EARTH:
        pos, vel = rk(truss_accel_no_mass, pos, vel, dt)
        t += dt
        arc_length = np.sqrt((pos[0]-pos_old[0])**2 + (pos[1]-pos_old[1])**2) 
        # uses pythogorus theorem to find the approx distance between adjacent points
        horizontal_distance += arc_length # increments approximate to total value
        pos_old = pos # updates the old position value
        pos_list.append(pos.copy())
        vel_list.append(vel.copy())
        t_list.append(t)

    return np.array(t_list), np.array(pos_list), np.array(vel_list), horizontal_distance

def main():
    dt = 1.0 # timestep (s)
    h0 = 130000.0 # initial altitude (m)
    v0 = 7800.0 # initial tangential velocity (m/s)
    mass = M_ISS + M_DV # ISS + deorbit vehicle (kg)

    init_pos = np.array([0.0, R_EARTH + h0])
    init_vel = np.array([v0, 0.0])

    t, pos, vel, hd = simulate_reentry(dt, init_pos, init_vel, mass)
    plot_position_earth(pos[:,0], pos[:,1])

    print("Reentry simulation with drag completed successfully.")
    print(f"Position array: ", pos)
    print(f"Velocity array:", vel)
    print(f"Simulation steps: {len(t)}")
    print(f"Final time: {t[-1]:.2f} s")
    print(f"Final altitude: {np.sqrt(pos[0,-1]**2 + pos[1,-1]**2) - R_EARTH:.2f} m")
    print("Horizontal distance the truss debris crosses from this point to splash down:", hd, "m")

if __name__ == "__main__":
    main()