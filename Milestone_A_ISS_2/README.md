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
The user can run ```main.py``` from the code itself, which will simulate the deorbit with an initial altitude of 275000m, an initial velocity of 7700m/s, a step interval of 1s, a orbital decay duration of 90 minutes, and a final burn duration of 60 minutes.

Alternatively, the user can run the program through the command line as follows:

```python main.py <initial altitude> <initial velocity> <step interval> <orbital decay duration> <final burn duration>```

This can be used to run the program with different inputs.

## Testing
The following tests cases were provided to us, all of them can be run by plugging the required variables into the respective assigned functions:

- Orbital Decay: initial altitude=400km, initial velocity=7670m/s, simulation time=90 min
- Final Burn: initial altitude=220km, initial velocity=7770m/s, simulation time=60 min, constant thrust=3236 N
- Re-Entry Trajectory: initial altitude=130km, initial velocity=7800m/s
- Rocket Trajectory: initial altitude=0m, initial velocity=0m/s, simulation time=8*burn_time

We used testing as a tool to resolve conflicts within our individual roles and with integration. For example, testing allowed us to ensure that our shared functions (drag, gravitational acceleration, and Runge-Kutta method) were all working properly and cooperated with our code. In some cases, testing showed that we weren't implementing arrays early enough to be used with these shared functions. Similarly, we had to test the ```main()``` function that implemented all of our roles together to ensure that each role's input built on the previous role's output and they all worked together to simulate the ISS's deorbit.

We also tried running the program with different inputs. For example, starting at a higher altitude meant that it took longer to reach the Earth. We used this testing to confirm that our program was modeling the physics correctly, and that it could function for a variety of different initial states.

One specific example is simulating final burn for 70 minutes instead of 60 minutes. This led to a final altitude of 115 km instead of a final altitude of 118 km, which is as expected when running this process for a longer duration. We tested other variables as well with different combinations to ensure the functions gave correct output.

The output is expected for each function because the functions return a correctly shaped graph that matches the list functions returned.


## Acknowledgements
Authors: Judah Brackin, Luke Burrow, Yiannis Konstantinou, Yuvraj Ruparel

Acknowledgements: Dr. Lipp

AI Use Statement: We did not use GenAI for this project.