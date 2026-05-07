# Assigned to Judah

from constants import *
from plot import plot_position_earth
from euler import euler
import math

def final_burn(init_alt, init_vel, sim_time_s, time_step):
    """
    Takes initial altitude, initial velocity, time for simulation, and resolution for
    sampling and simulating the data of deorbit.
    Returns time, x position, y position, x velocity, y velocity as lists

    Sim time is 60 minutes for milestone C 
    """

    x_pos = R_EARTH + init_alt
    y_pos = 0
    x_vel = 0
    y_vel = init_vel

    time_list = []
    x_pos_list = []
    y_pos_list = []
    x_vel_list = []
    y_vel_list = []

    n_steps = int(sim_time_s / time_step) + 1

    for step in range(n_steps): # sim time is 60*60+1 for test case
        time_list.append(step*time_step)
        x_pos_list.append(x_pos)
        y_pos_list.append(y_pos)
        x_vel_list.append(x_vel)
        y_vel_list.append(y_vel)

        # finds scalar radius and velocity
        r = math.hypot(x_pos, y_pos)
        v = math.hypot(x_vel, y_vel)

        # avoid div zero error, otherwise calculate acceleration based on formula
        if v == 0:
            a_x = 0
            a_y = 0
        else:
            a_x = (-9.1 * x_pos / r
                - 0.5 * RHO_LEO * C_D_ISS * AREA_ISS * v * x_vel / (M_ISS + M_DV)
                - THRUST * x_vel / ((M_ISS + M_DV) * v))

            a_y = (-9.1 * y_pos / r
                - 0.5 * RHO_LEO * C_D_ISS * AREA_ISS * v * y_vel / (M_ISS + M_DV)
                - THRUST * y_vel / ((M_ISS + M_DV) * v))

        # find next values with euler function
        x_data = euler(a_x, x_vel, x_pos, time_step)
        x_vel = x_data[0]
        x_pos = x_data[1]

        y_data = euler(a_y, y_vel, y_pos,time_step)
        y_vel = y_data[0]
        y_pos = y_data[1]

    # Output time, x_pos, y_pos, x_vel, y_vel as lists
    return time_list, x_pos_list, y_pos_list, x_vel_list, y_vel_list

def main():
    """
    Main function to set up initial states and call simulation.
    Plots data.
    """
    data = final_burn(220000, 7770, 60*60, 0.1)
    plot_position_earth(data[1],data[2])

if __name__ == '__main__':
    main()
