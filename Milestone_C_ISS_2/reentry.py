# Assigned to Yuvraj

from constants import *
from plot import plot_position_earth
import math
import matplotlib as plt

def gravity_force(mass, x, y):
    """
    Calculates force due to gravity given a mass, x and y position.
    Returns tuple of x and y forces.
    """

    # calculates the radius based on x and y value
    r = math.sqrt(x**2 + y**2)

    # calculates the x and y magnitudes of force using the formula
    F_x = -G * M_EARTH * mass * x / r**3 
    F_y = -G * M_EARTH * mass * y / r**3

    # returns the force values calculated
    return F_x, F_y

def simulate_reentry(dt, h0, v0, mass):
    """
    Main function to simulate reentry. 
    Takes time step, initial altitude, initial velocity, and mass.
    Returns lists of time, x and y position, x and y velocity.
    """
    # initial conditions for lists
    x, y = [0.0], [R_EARTH + h0]  # position (m)
    vx, vy = [v0], [0.0]          # velocity (m/s)
    t = [0.0]                     # time (s)

    for time in range(5400+1): # 90 minutes
        # caculate current radius of ISS
        r = math.sqrt(x[-1]**2 + y[-1]**2)
        if r <= R_EARTH:  # stop when ISS reaches Earth surface
            break

        # call gravity_force function
        F_x, F_y = gravity_force(mass, x[-1], y[-1])

        # convert force to accelration
        a_x = F_x / mass
        a_y = F_y / mass

        # update velocity and position using euler equations into the list
        vx_new = vx[-1] + a_x * dt
        vy_new = vy[-1] + a_y * dt
        x_new = x[-1] + vx_new * dt
        y_new = y[-1] + vy_new * dt

        vx.append(vx_new)
        vy.append(vy_new)
        x.append(x_new)
        y.append(y_new)
        t.append(t[-1] + dt)

    # return t, x, y, vx, and vy lists
    return t, x, y, vx, vy

def main():
    """
    Calls function. Sets up input variables.
    Prints lists and plots data
    """
    # assign values to variables
    dt = 1.0                  # timestep (s)
    h0 = 130000               # initial altitude (m)
    v0 = 7800                 # initial tangential velocity (m/s)
    mass = M_ISS + M_DV       # ISS + deorbit vehicle (kg)
    
    # call simulate_reentry function
    t, x, y, vx, vy = simulate_reentry(dt, h0, v0, mass)
    plot_position_earth(x, y)

    # outputs
    print("Reentry simulation completed and plotted successfully.")
    print("Time:",t)
    print("x-Position:",x)
    print("y-Position:",y)
    print("x-velocity:",vx)
    print("y-velocity:",vy)

if __name__ == '__main__':
    main()