from constants import *
import numpy as np

def rk(accel, pos, vel, dt):
    # k terms affect velocity
    k1 = accel(pos, vel)
    l1 = vel

    k2 = accel(
        pos + 0.5 * dt * l1,
        vel + 0.5 * dt * k1
    )
    l2 = vel + 0.5 * dt * k1

    k3 = accel(
        pos + 0.5 * dt * l2,
        vel + 0.5 * dt * k2
    )
    l3 = vel + 0.5 * dt * k2

    k4 = accel(
        pos + dt * l3,
        vel + dt * k3
    )
    l4 = vel + dt * k3

    vel_new = vel + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)
    pos_new = pos + (dt / 6) * (l1 + 2*l2 + 2*l3 + l4)

    return pos_new, vel_new


def drag_accel(vel, pos, mass):
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

    return drag_vec / (mass)

def gravity_accel(pos):
    """
    Computes gravitational acceleration vector at position pos
    using Newton's law of universal gravitation.
    """
    r = np.sqrt(pos[0]**2 + pos[1]**2)
    return -G * M_EARTH * pos / r**3