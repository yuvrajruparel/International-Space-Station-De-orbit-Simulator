# ISS Deorbit: C Milestone

For this milestone, each team member will perform a simulation using Euler's method that starts from initial conditions and evolves with time, according to the physical principles of gravity, drag, and rocket thrust. Consider the two dimensional problem, such that the Earth is in an x-y plane, forces act only in two directions, and gravity acts on the ISS directed toward the center of the Earth. For this milestone, each role will also make some simplifying assumptions about the physics, described below.

Each team member should write a program with a main function and at least one other function that actually performs the simulation. Main should set up the simulation parameters, call the simulation function, and plot the results. The simulation function should return the requested lists representing a trajectory.

::: {.callout-important}
For the C milestone, the use of outside packages for this program is not permitted.  Only the Python standard library can be used.
:::

## Team Roles

Below are the detailed specifications by each team member's role.

### Orbital decay

Given an initial altitude and velocity for the ISS, perform a 2D simulation of the vehicle trajectory under force of gravity. 

For this milestone, make the following assumptions:

- Drag is negligible.
- Gravity is modeled with Newton's law of universal gravitation.

The simulation should output the time, x-position, y-position, x-velocity, and y-velocity as list data types. Plot the x- and y-position of the ISS.

Filename: `orbital_decay.py`

Try the following initial conditions and parameters:

* Initial altitude 400 km
* Initial velocity 7670 m/s (orthogonal to radial direction)
* Simulation time 90 min


### Final burn

Given deorbit vehicle parameters, simulate the final burn phase of the deorbit, when the deorbit vehicle is docked to the ISS. Perform a 2D simulation under forces of gravity, drag, and thrust. 

For this milestone, make the following assumptions:

- Acceleration due to gravity is constant and approximately 9.1 m/s^2. 
- Air density is constant for LEO. 
- Thrust is constant and directed to decelerate the ISS, oriented opposite the velocity vector. 

The simulation should output time, x-position, y-position, x-velocity, and y-velocity as list data types. Plot the x- and y- position of the ISS + deorbit vehicle, and determine the final altitude.

Filename: `final_burn.py`

Try the following initial conditions and parameters:

* Initial altitude 220 km
* Initial velocity 7770 m/s (orthogonal to radial direction)
* Simulation time 60 min
* Constant thrust 3236 N 
* Use drag coefficient of ISS, area of ISS, and mass of ISS and deorbit vehicle combined

### Re-entry trajectory

Given initial altitude and x- and y-velocity, simulate the re-entry phase of the deorbit. Perform a 2D simulation of ISS re-entry, under force of gravity. 

For this milestone, make the following assumptions:

- Drag is negligible.
- The ISS and deorbit vehicle remain docked for the duration of the descent.
- The simulation stops when the mass reaches zero altitude.

The simulation should output time, position, and velocity as list data types. Plot the x- and y- position of the mass.

Filename: `reentry.py`

Try the following initial conditions and parameters:

* Initial altitude 130 km
* Initial velocity 7800 m/s (orthogonal to radial direction)
* Use ISS parameters + deorbit vehicle

### Rocket trajectory

Given rocket parameters, perform a 1D simulation of a rocket trajectory under forces of gravity, drag, and rocket thrust, according to a simplified rocket equation. 

For this milestone, make the following assumptions:

- Thrust is constant until burn time.
- Air density varies with altitude, according to a decaying exponential model.

The simulation should output time, altitude, and velocity as list data types. Plot the altitude vs. time of the rocket, identifying the maximum altitude.

Filename: `rocket.py`

Try the following initial conditions and parameters:

* Initial altitude 0 m
* Initial velocity 0 m/s
* Simulation time `8*burn_time`

## Resources

- [Euler's Method for Numerical Simulation](eulers_method.ipynb)
- [Physics for Aerospace](physics.pdf){.external target="_blank"}
- <https://www.nasa.gov/faqs-the-international-space-station-transition-plan/>{.external target="_blank"}
- <https://www.nasa.gov/current-reports-and-transcripts/>{.external target="_blank"}
- [ISS+Deorbit+USOS+Concept+of+Operations+Overview.pdf](ISS+Deorbit+USOS+Concept+of+Operations+Overview.pdf){.external target="_blank"}



