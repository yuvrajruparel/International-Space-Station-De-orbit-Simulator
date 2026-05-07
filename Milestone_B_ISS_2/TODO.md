
ISS Deorbit: B Milestone
Overview

For the B Milestone, you will improve your simulations by using NumPy arrays, making the physical models more realistic, and integrating the individual parts of your project.

When the combined program is run, the full simulation from launching the deorbit vehicle, to orbital decay of the ISS, to docking, to re-entry will be modeled and visualized for a user.
ImportantAI Policy

Code allowable use: AI Tutor
AI can be used to answer questions a TA would be willing to answer. You may ask conceptual questions.

You may not use AI to generate code, either in part or wholesale.

Documentation allowable use: AI-assisted editing
AI can be used to make improvements to the clarity or quality of your documentation (README).
Specifications
NumPy Arrays

First, update your simulations to use NumPy arrays. If you know the number of simulation steps at the start, you can create arrays of the correct size. If you have a stopping condition and do not know how many steps, you can either use lists and convert to arrays when finished iterating, or you can resize the arrays (doubling the size each time you run out of room—concatenate and empty_like may be useful).

We suggest combining
and position into one array with two rows (similarly, combining and

velocity into one array with two rows). This will reduce the number of parameters you need to pass and will help simplify the advanced numerical integration that is part of the A Milestone.
Physics

Each role should now use the full physical model. For example, if you ignored drag in the previous milestone, include it for this one. Similarly, if you assumed constant acceleration due to gravity, now calculate it as a function of position from Earth’s center. Each team member should have familiarity with at least one of these they can share with others:

    Gravity: use Newton’s law of universal gravitation.
    Drag: use the model where drag is proportional to the square of velocity. Use a model for atmospheric density that changes with altitude and approaches density at sea level for zero altitude and approaches zero for infinity altitude.

Note: these functions are good candidates for shared code, since multiple roles will need to use them!
Integration

Each stage of the simulation will provide the initial conditions for the next. The stages are:

    Natural orbital decay (use combined mass of ISS and DV, assuming rendezvous has already occured)
        Initial altitude 275 km
        Initial velocity 7700 m/s
        Simulation time 90 min
    Final burn
        Initial position determined from final position of (1)
        Initial velocity determined from final velocity of (1)
        Simulation time 60 min
    Re-entry
        Initial position determined from final position of (2)
        Initial velocity determined from final velocity of (2)
        Simulation runs until 0 altitude
    Launch vehicle rocket
        Initial altitude 0 km
        Initial velocity 0 m/s
        Simulation time 

The simulation parameters suggested should result in splashdown. For the launch vehicle, you want to show that it attains at least the rendezvous altitude (around 400 km). The estimated mass of propellant is more than enough for task, so determine what percent of the propellant mass is really necessary for rendezvous.

The final integrated program should:

    Have one main file to run the program
    Simulate the deorbit trajectory through all stages
    Print the final altitude and velocity magnitude after each stage
    Plot the trajectories of each stage over the Earth in the xy plane
    Plot the trajectory of the launch vehicle showing altitude vs. time

Testing note: final burn and re-entry roles should not wait until orbital decay is ready to test your code! Your file can have its own main (that is not run when the module is imported) that tests starting from the same initial conditions as the C Milestone.

You are strongly encouraged to write code that can be shared by all the roles.

We suggest copying your C Milestone code into a subdirectory and then modifying each individual module to meet the new specifications for the B Milestone.
Documentation

The B Milestone also asks you to document and organize your work. Here are the requirements for how to do so.
File Organization

The team Git repository should be clearly organized. A README.md should be at the root level. Move your C Milestone work to a subdirectory, and organize your B Milestone code as follows:

├── README.md
├── common.py
├── main.py
├── role1.py
├── role2.py
├── role3.py
├── c_ms
│   ├── role1.py
│   ├── role2.py
│   ├── role3.py

Note: You will replace the roleX.py file names with your own files, and common.py represents any module that is shared between the others, but you do not need to use that name.
Version Control

Each team member should have a minimum of three commits with significant changes to the project.
NoteCommit Messages

Commit messages should describe what changes were made.
README

The README.md, which is markdown file, has a title and all required sections:

    Description
    Background
        Provides context and scientific principles for your problem. About one paragraph per role.
    Features
        Describes what your project does. This should be specific in what methods your solution uses but does not need to discuss the code implementation.
    Usage
        Tells a user how to run your program. Includes the command to run your combined program (format by indenting four spaces or enclosing in a ``` fence). If the program takes command line arguments or user input, describe how this works and what the user needs to do to interact with your program.
    Testing
        Explains what test cases you are providing and discusses whether your program passes them and how you know. Include also the command to run your test cases.
    Acknowledgements
        Names the authors and acknowleges those who have helped the team.
        Includes an AI use statement specifying whether and how generative AI was used in the project.

See this resource for markdown format https://www.markdownguide.org/basic-syntax

Be sure to address any feedback from the previous sprint to deliver a thorough README.md file.
Docstrings

Each function should have a docstring, i.e. a comment in triple quotes directly under the function declaration. Helper functions have a one-line docstring that describes what they do. Important functions have a multi-line docstring with description of function, as well as parameters and return values, as specified in PEP: https://peps.python.org/pep-0257/

Elsewhere in the code, write a comment for anything complex or unusual to help the reader understand your approach.
