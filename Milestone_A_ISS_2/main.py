import sys
import numpy as np
from plot import plot_position_earth, plot_simple
from constants import *
import matplotlib.pyplot as plt

from rk_orbital_decay import orbital_decay
from rk_final_burn import final_burn
from rk_reentry import simulate_reentry
from rk_rocket_trajectory import extract_altitude_from_pos, rocket_trajectory, find_minimum_fuel_percentage


def main(alt, vel, dt, time_od, time_fb):
    # Call orbital decay
    o_time, o_pos, o_vel = orbital_decay(vel, alt, time_od, dt)

    print("-------------------------------------")
    print("Orbital Decay:")
    print("Final altitude:", np.linalg.norm(o_pos[:,-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(o_vel[:,-1]))
    print("-------------------------------------")

    plot_position_earth(o_pos[0],o_pos[1])

    # Call final burn with output from orbital decay
    f_time, f_pos, f_vel = final_burn(o_pos[:,-1], o_vel[:,-1], time_fb, dt)

    print("Final Burn:")
    print("Final altitude:", np.linalg.norm(f_pos[:,-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(f_vel[:,-1]))
    print("-------------------------------------")

    plot_position_earth(f_pos[0],f_pos[1])

    # Call reentry with output from reentry
    re_time, re_pos, re_vel, horizontal_distance = simulate_reentry(dt, f_pos[:,-1], f_vel[:,-1], M_ISS+M_DV)

    print("Re-entry:")
    print("Final altitude:", np.linalg.norm(re_pos[-1]) - R_EARTH)
    print("Final velocity:", np.linalg.norm(re_vel[-1]))
    print(f"Horizontal distance the truss debris crosses from this point to splash down: {(horizontal_distance/1000):.2f}km")
    print("-------------------------------------")

    plot_position_earth(re_pos[:,0],re_pos[:,1])

    same_dim_re = re_pos.T
    tot_pos = np.hstack([o_pos, f_pos, same_dim_re])

    # plot position earth with labels added
    th = np.linspace(0, 2*np.pi,100)
    xearth = R_EARTH*np.cos(th)
    yearth = R_EARTH*np.sin(th)

    plt.plot(xearth, yearth)
    plt.plot(o_pos[0][0], o_pos[1][0], 'o', o_pos[0], o_pos[1], o_pos[0][-1], o_pos[1][-1], color= 'blue')
    plt.plot(f_pos[0][0], f_pos[1][0], 'o', f_pos[0], f_pos[1], f_pos[0][-1], f_pos[1][-1], color= 'red')
    plt.plot(same_dim_re[0][0], same_dim_re[1][0], 'o', same_dim_re[0], same_dim_re[1], same_dim_re[0][-1], same_dim_re[1][-1], 'g^')

    plt.text(o_pos[0][0], o_pos[1][0], 'Orbital Decay')
    plt.text(f_pos[0][0], f_pos[1][0], 'Final Burn')
    plt.text(same_dim_re[0][0], same_dim_re[1][0], 'Re-Entry')

    plt.axis('equal')
    plt.show()



    # Setup for running rocket (more complicated):


    target_altitude = 400_000   # 400 km

    # find minimum fuel percentage
    min_fuel_pct = find_minimum_fuel_percentage(target_altitude, dt)

    init_pos = np.array([R_EARTH, 0.0])
    init_vel = np.array([0.0, 0.0])

    # compute burn time for the minimum fuel percentage
    m_i = M_0_LV
    effective_mass_ratio = 1 + (MASS_RATIO_LV - 1) * min_fuel_pct
    m_f = m_i / effective_mass_ratio
    t_burn_min = (m_i - m_f) / M_DOT_E_LV


    # run for 8*t_burn_min
    sim_time = 8 * t_burn_min
    t, pos, vel = rocket_trajectory(init_pos, init_vel, sim_time, dt, t_burn_min)


    altitude_m = extract_altitude_from_pos(pos)
    
    idx = len(altitude_m) - 1  # Default to end if never reaches
    for i in range(len(altitude_m)):
        if altitude_m[i] >= target_altitude:
            idx = i
            break  
    
    t = t[: idx+1]
    pos = pos[:, : idx+1]
    vel = vel[:, : idx+1]
    altitude = altitude_m[: idx+1] / 1000   # km

    print("Launch Vehicle:")
    print(f"Max altitude: {np.max(altitude):.2f} km")
    print(f"Final altitude: {altitude[-1]:.2f} km")
    print(f"Final velocity: {np.linalg.norm(vel[:, -1]):.1f} m/s")
    print(f"Minimum fuel percentage to exceed 400 km: {min_fuel_pct*100:.2f}%")
    print("-------------------------------------")

    capped_alt = np.clip(altitude, 0, 400)
    plot_simple(t, capped_alt)

if __name__ == "__main__":
    if len(sys.argv) == 6:
        init_alt, init_vel, dt, time_od, time_fb = sys.argv[1:]
        init_alt = float(init_alt)
        init_vel = float(init_vel)
        dt = float(dt)
        time_od = float(time_od)
        time_fb = float(time_fb)

        main(init_alt, init_vel, dt, time_od, time_fb)
    else:
        main(275000, 7700, 1, 90*60, 60*60)