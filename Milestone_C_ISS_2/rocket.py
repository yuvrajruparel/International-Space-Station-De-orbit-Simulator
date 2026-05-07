# Assigned to Yiannis

import math
from constants import *    
from plot import plot_simple  


def calculated_burn_time():
    """
    Simulates burn time.
    Outputs burn time and total time.
    """
    m_initial = M_0_LV
    mass_ratio = MASS_RATIO_LV
    m_dot = M_DOT_E_LV  # exhaust mass flow rate (kg/s)

    # final mass
    m_final = m_initial / mass_ratio

    # burn time (s)
    burn_time = (m_initial - m_final) / m_dot

    # total simulation time (8 × burn time, as required)
    total_time = 8 * burn_time

    return burn_time, total_time


def air_density(altitude):
    """
    Function to calculate air density for a given altitude.
    Returns air density.
    """
    if altitude < 0:
        altitude = 0
    return RHO_0 * math.exp(-altitude / H_0)


def rocket_trajectory(dt):
    """
    Main simulation of rocket trajectory given a time step.
    Returns lists of time, x and y position, as well as burn time and total time.
    """
    # calculate burn and total time
    burn_time, total_time = calculated_burn_time()

    # initial conditions
    t = 0.0        # time (s)
    y = 0.0        # altitude (m)
    v = 0.0        # velocity (m/s)

    # store data for plotting
    t_list = [t]
    y_list = [y]
    v_list = [v]

    # Constant thrust
    T = M_DOT_E_LV * I_SP_LV * g_0 
    print(f"Thrust: {T:.2f} N")

    # simulation loop
    n_steps = int(total_time / dt)

    for _ in range(n_steps):
        # compute air density based on altitude
        rho = air_density(y)

        # drag force
        Fd = 0.5 * rho * C_D_LV * AREA_LV * v * abs(v)

        # determine current mass and thrust
        if t <= burn_time:
            m = M_0_LV - M_DOT_E_LV * t  
            Ft = T                       # thrust on
        else:
            m = M_0_LV - M_DOT_E_LV * burn_time 
            Ft = 0.0                      # thrust off

        # gravitational force
        Fg = m * g_0

        # net acceleration 
        a = (Ft - Fd - Fg) / m

        # Euler 
        v_next = v + a * dt
        y_next = y + v * dt
        t_next = t + dt

        # stop if rocket hits the ground again
        if y_next < 0:
            break

        # update variables
        t, y, v = t_next, y_next, v_next

        # Save results
        t_list.append(t)
        y_list.append(y)
        v_list.append(v)

    return t_list, y_list, v_list, burn_time, total_time


def main():
    """
    Main function to set up variables and call the simulation.
    Plots altitude and velocity graphs against time.
    Prints summary of results.
    """
    # parameter
    dt = 0.1  # seconds

    # run simulation
    t, y, v, burn_time, total_time = rocket_trajectory(dt)

    # find max altitude
    max_alt = max(y)
    t_max = t[y.index(max_alt)]

    # print summary
    print("\n--- Simulation Summary ---")
    print(f"Burn time: {burn_time:.2f} s")
    print(f"Total simulation time: {total_time:.2f} s")
    print(f"Maximum altitude: {max_alt/1000:.2f} km at t = {t_max:.1f} s")

    # lot altitude vs time (km)
    alt_km = [alt / 1000 for alt in y]
    plot_simple(t, alt_km)

    # plot velocity vs time (m/s)
    plot_simple(t, v)


if __name__ == "__main__":
    main()
