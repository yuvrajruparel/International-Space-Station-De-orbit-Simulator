# Assigned to Luke

import numpy as np
from constants import *
from euler import euler
from plot import plot_position_earth

def orbital_decay(velocity_initial, altitude):
    """
    Simulates orbital decay given initial velocity and altitude.
    Returns lists of time, x and y position, x and y velocity.
    """
    #Variables setup

    radius=altitude+R_EARTH

    x_pos = radius
    y_pos = 0
    x_vel = 0
    y_vel = velocity_initial

    time_array=np.array([])
    x_pos_array=np.array([])
    y_pos_array=np.array([])
    x_vel_array=np.array([])
    y_vel_array=np.array([])

    #time_array=np.empty_like([5400,0])
    #pos_array=np.empty_like([5400,1])
    #vel_array=np.empty_like([5400,1])
    
    for t in range(10 * (5400 + 1)):

        time_array=np.append(time_array, t)
        x_pos_array=np.append(x_pos_array, x_pos)
        y_pos_array=np.append(y_pos_array, y_pos)
        x_vel_array=np.append(x_vel_array, x_vel)
        y_vel_array=np.append(y_vel_array, y_vel)

        #time_array[t]=t
        #pos_array[t]=x_pos
        #pos_array[t,1]=y_pos
        #vel_array[t]=x_vel
        #vel_array[t,1]=y_vel

        radius = np.sqrt((x_pos**2)+(y_pos**2))

        x_grav_acceleration=-G*(M_EARTH/(radius**3))*x_pos
        y_grav_acceleration=-G*(M_EARTH/(radius**3))*y_pos

        x_drag_acceleration, y_drag_acceleration=find_drag(x_pos, y_pos, x_vel, y_vel, radius)

        x_acceleration=x_grav_acceleration+x_drag_acceleration
        y_acceleration=y_grav_acceleration+y_drag_acceleration

        dt = 0.1
        x_vel, x_pos = euler(x_acceleration, x_vel, x_pos, dt)
        y_vel, y_pos = euler(y_acceleration, y_vel, y_pos, dt)

    

    pos = np.vstack((x_pos_array, y_pos_array))
    vel = np.vstack((x_vel_array, y_vel_array))

    return time_array, pos, vel
    #return time_array, pos_array, vel_array

def find_drag(x_pos, y_pos, x_vel, y_vel, radius):
    """
    Finds acceleration due to drag given velocities in x and y directions and radius.
    """
    #Variables setup
    radius=np.sqrt((x_pos**2)+(y_pos**2))
    height=radius-R_EARTH
    velocity=np.sqrt((x_vel**2)+(y_vel**2))
    if velocity == 0:
        return 0.0, 0.0
    rho=RHO_0*np.exp(-height/(H_0))

    drag_mag = 0.5 * rho * C_D_ISS * AREA_ISS * velocity**2

    x_drag_acceleration = -drag_mag * x_vel / (velocity * (M_ISS + M_DV))
    y_drag_acceleration = -drag_mag * y_vel / (velocity * (M_ISS + M_DV))

    return x_drag_acceleration, y_drag_acceleration

def main():
    """
    Main function to set up initial conditions.
    Also calls simulation and plots results.
    """
    altitude = 275000
    velocity_initial = 7700
    
    time,pos,vel =orbital_decay(velocity_initial, altitude)
    plot_position_earth(pos[0],pos[1])

if __name__ == '__main__':
    main()
