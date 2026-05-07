# Assigned to Judah

import numpy as np
from constants import *
from euler import euler
from plot import plot_position_earth


def gravity_accel(pos):
    """
    Computes gravitational acceleration vector at position pos
    using Newton's law of universal gravitation.
    """
    r = np.sqrt(pos[0]**2 + pos[1]**2)
    return -G * M_EARTH * pos / r**3


def drag_accel(vel, pos):
    """
    Computes drag acceleration vector.
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

    drag_mag = 0.5 * rho * C_D_ISS * AREA_ISS * v**2
    drag_vec = -drag_mag * (vel / v)

    return drag_vec / (M_ISS + M_DV)


def thrust_accel(vel):
    """
    Computes thrust acceleration opposite the direction of motion.
    """
    v = np.sqrt(vel[0]**2 + vel[1]**2)
    if v == 0:
        return np.array([0.0, 0.0])

    thrust_vec = -THRUST * (vel / v)
    return thrust_vec / (M_ISS + M_DV)


def final_burn(init_pos, init_vel, sim_time_s, time_step):
    """
    Uses numpy arrays to simulate final burn.
    Takes init_pos, init_vel, sim_time_s, time_step
    Returns t, pos, vel
    """
    # number of steps
    N = int(sim_time_s / time_step) + 1

    # create arrays
    t = np.linspace(0, sim_time_s, N)
    pos = np.zeros((2, N))
    vel = np.zeros((2, N))

    # initialize in orbit
    pos[:, 0] = init_pos
    vel[:, 0] = init_vel

    # iterate
    for i in range(N - 1):

        # compute total acceleration
        a_g = gravity_accel(pos[:, i])
        a_d = drag_accel(vel[:, i], pos[:, i])
        a_t = thrust_accel(vel[:, i])

        a_total = a_g + a_d + a_t

        # Euler update for each dimension
        vel_x, pos_x = euler(a_total[0], vel[0, i], pos[0, i], time_step)
        vel_y, pos_y = euler(a_total[1], vel[1, i], pos[1, i], time_step)

        vel[:, i+1] = np.array([vel_x, vel_y])
        pos[:, i+1] = np.array([pos_x, pos_y])

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
