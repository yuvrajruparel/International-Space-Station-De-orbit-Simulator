# International-Space-Station-De-orbit-Simulator
## What is this project about?
The International Space Station (ISS) is a space station in low Earth orbit, maintained by five countries, for microgravity and space experiments. In the next decade NASA will transition to commercial space operations. When the ISS program is concluded, the ISS needs to be safely deorbited to avoid hitting populated areas of Earth. To meet the primary objective of responsible re-entry into a depopulated area of the ocean, the chosen approach for a safe decommissioning is “combination of natural orbital decay, intentionally lowering the altitude of the station likely using current propulsive elements, and then execution of a re-entry maneuver for final targeting and to control the debris footprint.” The re-entry maneuver requires additional thrust, so SpaceX is designing a US Deorbit Vehicle that will dock with the ISS and help control the re-entry.

To recreate the task of planning a safe re-entry, this project has 4 roles:
* Simulate the ISS in natural orbital decay
* Simulate a launch vehicle trajectory to meet the ISS
* Simulate the final burn for the deorbit maneuver
* Simulate the breakup and reentry of the ISS

When integrated, this project will be able to simulate the trajectory for re-entry.

## What special skills will I gain?
In addition to the algorithmic and programming skills required by all of the projects, after the successful completion of this project, you will be able to:

* Model orbital mechanics and rockets with the forces of gravity, drag, and thrust.
* Implement a numerical method to solve a differential equation. Note: this does not require you to have done any coursework in differential equations!
* Use NumPy arrays and methods for efficient numerical calculation and Matplotlib to create visualizations of results.

## What will I do for each milestone?
The D milestone comprises domain knowledge for this problem.

To achieve the C milestone, each team member will perform a simulation using Euler’s method that starts from initial conditions and evolves with time, according to the physical principles of gravity, drag, and rocket thrust. For this level, you will make some simplifying assumptions about the physics.

After you complete the C milestone, to achieve the B milestone, you will improve your numerical simulation by removing some of the simplifying assumptions about the physics and implementing the simulation with more efficient NumPy arrays. Your team will integrate their separate parts to plot the full trajectory of the ISS descent.

The A milestone adds specifications, such as using a more accurate numerical method and making your program more flexible by taking command line arguments for the initial conditions and simulation parameters.