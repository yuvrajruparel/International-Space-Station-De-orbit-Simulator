from np_orbital_decay import *
from np_final_burn import *
from np_reentry import *
from np_rocket import *
from constants import *
from plot import save_plot_position_earth

import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    Main function to call all subroutines with previous states.
    Saves figures and prints final values.
    """


    # Define initial conditions
    init_alt = 275000
    init_vel = 7700
    mass = M_ISS + M_DV



    # Call orbital decay
    o_time, o_pos, o_vel = orbital_decay(init_vel, init_alt)

    print("-------------------------------------")
    print("Orbital Decay:")
    print("Final altitude:", np.linalg.norm(o_pos[:,-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(o_vel[:,-1]))
    print("-------------------------------------")

    save_plot_position_earth(o_pos[0],o_pos[1],"orbital_decay.png")


    # Call final burn with output from orbital decay
    f_time, f_pos, f_vel = final_burn(o_pos[:,-1], o_vel[:,-1], 60*60, 1)

    print("Final Burn:")
    print("Final altitude:", np.linalg.norm(f_pos[:,-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(f_vel[:,-1]))
    print("-------------------------------------")

    save_plot_position_earth(f_pos[0],f_pos[1],"final_burn.png")



    # Call reentry with output from reentry
    re_time, re_pos, re_vel = simulate_reentry(1, f_pos[:,-1], f_vel[:,-1], mass)

    print("Re-entry:")
    print("Final altitude:", np.linalg.norm(re_pos[:,-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(re_vel[:,-1]))
    print("-------------------------------------")

    save_plot_position_earth(re_pos[0,:],re_pos[1,:],"reentry.png")


    dt = 0.1
    t, y, v, r_final, v_final = rocket_trajectory(dt)

    print("Launch Vehicle:")
    print(f"Max altitude: {np.max(y)/1000:.2f} km")
    print(f"Final altitude: {y[-1]/1000:.2f} km")
    print(f"Final velocity: {v[-1]:.1f} m/s")
    print("-------------------------------------")

    plt.figure()
    plt.plot(t,y)
    plt.savefig("figs/rocket.png")

    print("Figures generated and saved.")





if __name__ == "__main__":
    main()