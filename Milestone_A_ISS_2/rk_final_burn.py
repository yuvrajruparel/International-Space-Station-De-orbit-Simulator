# Assigned to Judah

import numpy as np
from constants import *
from shared_funcs import *
from plot import plot_position_earth

def thrust_accel(vel):
    """
    Computes thrust acceleration opposite the direction of motion.
    """
    v = np.sqrt(vel[0]**2 + vel[1]**2)
    if v == 0:
        return np.array([0.0, 0.0])

    thrust_vec = -THRUST * (vel / v)
    return thrust_vec / (M_ISS + M_DV)

def total_accel(pos, vel):
    return (
        gravity_accel(pos)
        + drag_accel(vel, pos, M_ISS + M_DV)
        + thrust_accel(vel)
    )

def final_burn(init_pos, init_vel, sim_time_s, time_step):
    """
    Uses numpy arrays to simulate final burn.
    Takes init_pos, init_vel, sim_time_s, time_step
    Returns t, pos, vel
    """
    # calculate of steps
    N = int(sim_time_s / time_step) + 1

    # create initial arrays
    t = np.linspace(0, sim_time_s, N)
    pos = np.zeros((2, N))
    vel = np.zeros((2, N))

    # start at correct position
    pos[:, 0] = init_pos
    vel[:, 0] = init_vel

    # iterate and calculate using rk
    for i in range(N - 1):
        pos[:, i+1], vel[:, i+1] = rk(total_accel, pos[:, i], vel[:, i], time_step)

    return t, pos, vel


def main():
    pos = [6639862.67294504, 543688.49162605] 
    vel = [-634.09978415, 7668.90654796]
    f_time, f_pos, f_vel = final_burn(pos, vel, 60*60, 1)

    print("Final Burn:")
    print("Final altitude:", np.linalg.norm(f_pos[:,-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(f_vel[:,-1]))

    plot_position_earth(f_pos[0],f_pos[1])


if __name__ == '__main__':
    main()
