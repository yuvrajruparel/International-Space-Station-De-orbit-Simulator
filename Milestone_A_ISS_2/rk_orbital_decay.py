#Assigned to Luke
from constants import *
from plot import plot_position_earth
from shared_funcs import *

def orbital_decay(velocity_initial, altitude, sim_time_s, time_step):
    """
    Simulates orbital decay given initial velocity and altitude.
    Returns lists of time, x and y position, x and y velocity.
    """
    #Variables setup

    numsteps = int(sim_time_s / time_step) + 1

    time_list = np.linspace(0, sim_time_s, numsteps)
    pos = np.zeros((2, numsteps))
    vel = np.zeros((2, numsteps))

    pos[:, 0] = [altitude + R_EARTH, 0]
    vel[:, 0] = [0, velocity_initial]

    for i in range(numsteps - 1):
        pos[:, i+1], vel[:, i+1] = rk(total_accel, pos[:, i], vel[:, i], time_step)

    return time_list, pos, vel

def total_accel(pos, vel):
    """
    Finds total acceleration using gravitational acceleration and drag acceleration functions.
    """
    accel = gravity_accel(pos) + drag_accel(vel, pos, M_ISS + M_DV)

    return accel

def main():
    """
    Main function to set up initial conditions.
    Also calls simulation and plots results.
    """
    altitude = 275000
    velocity_initial = 7700

    t, pos, vel = orbital_decay(velocity_initial, altitude, 90*60, 0.1)
    plot_position_earth(pos[0],pos[1])

if __name__ == '__main__':
    main()