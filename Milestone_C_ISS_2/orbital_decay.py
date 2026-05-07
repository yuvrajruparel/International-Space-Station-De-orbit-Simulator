from constants import *
from plot import plot_position_earth
from euler import euler
import math

#orbital decay function
def orbital_decay(velocity_initial, altitude):
    """
    Simulates orbital decay given initial velocity and altitude.
    Returns lists of time, x and y position, x and y velocity.
    """
    # Variables setup

    radius=altitude+R_EARTH

    x_pos = radius
    y_pos = 0
    x_vel = 0
    y_vel = velocity_initial

    time_list = []
    x_pos_list = []
    y_pos_list = []
    x_vel_list = []
    y_vel_list = []

    for t in range(5400+1): # 90 minutes
        time_list.append(t)
        x_pos_list.append(x_pos)
        y_pos_list.append(y_pos)
        x_vel_list.append(x_vel)
        y_vel_list.append(y_vel)

        radius = math.hypot(x_pos, y_pos)
        
        x_acceleration=-G*(M_EARTH/(radius**3))*x_pos
        y_acceleration=-G*(M_EARTH/(radius**3))*y_pos

        x_vel, x_pos = euler(x_acceleration, x_vel, x_pos)

        y_vel, y_pos = euler(y_acceleration, y_vel, y_pos)

    return time_list, x_pos_list, y_pos_list, x_vel_list, y_vel_list


def main():
    """
    Main function to set up initial conditions.
    Also calls simulation and plots results
    """
    velocity_initial=7670
    altitude=400000
    data = orbital_decay(velocity_initial, altitude)
    plot_position_earth(data[1],data[2])
    

if __name__ == '__main__':
    main()
