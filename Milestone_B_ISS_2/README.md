# ISS Deorbit 2

## Description
This project will simulate the deorbit process for the International Space Station (ISS) in 2031. There are three stages to be modeled: orbital decay, final burn, and reentry. The rocket behavior will also be modeled as it is necessary for a complete deorbit simulation

## Background
The project will be used to simulate the deorbit of the ISS such that it will land in an uninhabited region. The mission is planned for 2031 but the desire is for completion as soon as possible. It will be overseen by all ISS partners (NASA, CSA, ESA, JAXA, and Roscosmos).

- Orbital decay is the gradual decrease in the altitude over time which slowly lowers its orbital energy. The involved scientific principles are: Newton's second law, Newton's law of universal gravitation, and aerodynamic drag.
- Final burn is the phase in which the de-orbit vehicle is docked and produces thrust to decelerate the ISS. The involved scientific principles are: Newton's law of universal gravitation, aerodynamic drag, and thrust.
- Re-Entry is the descent into Earth's atmosphere until the ISS reaches an altitude of zero. It is designed to ensure the debris lands in a predetermined, uninhabited area. The involved scientific principles are: Newton's law of universal gravitation, aerodynamic drag, and thrust.
- Rocket trajectory simulates a vehicle being launched from the Earth's surface to the altitude of the ISS. The involved scientific principles are: Newton's law of universal gravitation, aerodynamic drag, thrust, and mass formula for a rocket.

## Features
The project breaks down each role into its own function, taking a set of inputs and producing a series of outputs.

- Orbital decay takes the initial parameters of an initial altitude, and initial velocity, and a simulation time of 90 minutes. The program uses the involved scientific principles to calculate and output the time, x- and y-positions, and x- and y-velocities, along with a plot modeling the ISS's orbital trajectory around Earth.
- Final burn takes the initial parameters of an initial altitude, initial velocity, and a simulation time of 60 minutes. The program uses the involved scientific principles to calculate and output time, x- and y- positions, and x- and y-velocities, along with a plot modeling the ISS's deceleration around Earth due to the de-orbit vehicle.
- Re-Entry takes the initial parameters of an initial altitude and an initial velocity. The program uses the involved scientific principles to calculate and output the time, position, and velocity, along with a plot of the ISS's descent.
- Rocket trajectory takes the initial parameters of initial altitude, initial velocity, and a simulation time. The program uses the involved scientific principles to calculate and output the time, altitude, and velocity, along with a plot modeling the altitude of the rocket over time.

## Usage
The user should run '''main()''' on main.py. This will interact with np_orbital_decay.py, np_final_burn.py, np_reentry.py, and np_rocket.py to simulate the entire deorbit process of the ISS. The program does not currently any user inputs because it using a given initial altitude of 275000m and initial velocity of 7700m/s.

## Testing
The following tests cases were provided to us, all of them can be run by plugging the required variables into the respective assigned functions:

Orbital Decay: initial altitude=400km, initial velocity=7670m/s, simulation time=90 min
Final Burn: initial altitude=220km, initial velocity=7770m/s, simulation time=60 min, constant thrust=3236 N
Re-Entry Trajectory: initial altitude=130km, initial velocity=7800m/s
Rocket Trajectory: initial altitude=0m, initial velocity=0m/s, simulation time=8*burn_time

We used testing as a tool to resolve conflicts within our individual roles and with integration. For example, orbital decay was originally producing a graph which got further away from Earth. However, through testing with print statements and commenting lines out, this problem was narrowed down to an error in the way drag was calculated. Similarly, testing was vital to ensure that our "main.py" function integrated each step properly so that they each built upon one another with starting and ending conditions and printed the correct outputs. Again, this was done through printing, commenting, and testing for the figure outputs.

The output is expected for each function because the functions return a correctly shaped graph that matches the list functions returned.
Because of this, we do not expect any errors, but we believe any that arise can be corrected in Phase 2 through team troubleshooting, collaboration, and use of the debugger.

## Acknowledgements
Authors: Judah Brackin, Luke Burrow, Yiannis, Konstantinou, Yuvraj Ruparel

Acknowledgements: Dr. Lipp

AI Use Statement: We did not use GenAI for this project.


