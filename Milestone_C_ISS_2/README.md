# ISS Deorbit 2

## Description

This project will simulate the deorbit process for the International Space Station (ISS) in 2031. There are three stages to be modeled: orbital decay, final burn, and reentry. The rocket behavior will also be modeled as it is necessary for a complete deorbit simulation. 

### Background

The project will be used to simulate the deorbit of the ISS such that it will land in an uninhabited region. The mission is planned for 2031 but the desire is for completion as soon as possible. It will be overseen by all ISS partners (NASA, CSA, ESA, JAXA, and Roscosmos).

The scientific principles behind the project include:
- Newton's second law
- Newton’s law of universal gravitation
- Aerodynamic drag
- Thrust and rocket modeling (via the rocket equation)
- Mass formula for a rocket

For each section, various parts of these principles will be ignored or simplified as they will not have much of an effect, depending on the section of deorbit being simulated.

### Features

Our project can be used to simulate the following:
- Orbital Decay (orbital_decay.py)
    - This simulates the natural decay under the force of gravity.
- Final Burn (final_burn.py)
    - This simulates the final burn phase, where the deorbit vehicle is docked and produces thrust to decelerate the ISS. Gravity, drag and thrust are modeled.
- Reentry (reentry.py)
    - This simulates the reentry phase until the ISS reaches an altitude of zero. Gravity is used to calculate the final position and velocity of the ISS.
- Rocket Trajectory (rocket.py)
    - This simulates the trajectory of the rocket using gravity, drag, and rocket thrust using the rocket equation.

## Usage

### [Orbital Decay]

- The program takes the inputs of the ISS's initial altitude above Earth and its initial velocity. The program also has a built in parameter of simulating for 90 minutes. 
- The expected outputs are the time (90 minutes), and lists for the x-position, y-position, x-velocity, and y-velocity, as well as a graph of the ISS's position in x and y dimensions.

### [Final Burn]

- The program takes the inputs of the ISS's initial altitude above Earth and its initial velocity, as well as the parameters of simulating for 60 minutes with constant thrust of 3236 N.
- The expected outputs are the time and lists for the x-position, y-position, x-velocity, and y-velocity. It will also output a plot of the ISS's position in x and y dimensions.

### [Re-Entry Trajectory]

- The program takes the inputs of the ISS's initial altitude above Earth and its initial velocity.
- The expected outputs are the time and lists for the position and velocity in x and y dimensions, as well as a plot of these positions.

### [Rocket Trajectory]

- The program takes the inputs of the ISS's initial altitude above Earth and initial velocity. It also has the paramets of simulating for 8 x the burn time.
- The expected outputs are the time, and lists for the altitude and velocity. It should also produce a plot of the rocket's altitude vs. time.

## Testing

The following tests cases were provided to us, all of them can be run by plugging the required variables into the respective assigned functions:
- Orbital Decay: initial altitude=400km, initial velocity=7670m/s, simulation time=90 min
- Final Burn: initial altitude=220km, initial velocity=7770m/s, simulation time=60 min, constant thrust=3236 N
- Re-Entry Trajectory: initial altitude=130km, initial velocity=7800m/s
- Rocket Trajectory: initial altitude=0m, initial velocity=0m/s, simulation time=8*burn_time

The output is expected for each function because the functions return a correctly shaped graph that matches the list functions returned.
Because of this, we do not expect any errors, but we believe any that arise can be corrected in Phase 2 through team troubleshooting collaboration use of the debugger.

## Roadmap

In Phase 2 and beyond, aside from fixing any errors, we plan to amend our current programs to make them fully accurate to real life. This includes accounting for drag in the Orbital Decay and Re-Entry Trajectory simulations, and accounting for changing thrust in the Final Burn and Rocket Trajectory simulations.
Eventually, we will also combine these four parts to fully simulate the ISS's De-Orbit.

## Authors and Acknowledgment

Authors: Judah Brackin, Luke Burrow, Yiannis Konstantinou, Yuvraj Ruparel
Acknowledgements: Dr Lipp, TA Ana