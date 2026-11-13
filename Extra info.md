Final Project Design Phase
Computer Science - Week 11
Oct 3, 2026 - Version 0.0.4



For complete instructions and project ideas, refer to the assignment in Canvas. Specifically, review the final project requirements before you continue below. If you have not reviewed the project requirements in Canvas (you might have to go to the modules view and check the current or past week's content), you will not be able to properly complete the parts below. In addition, it may be helpful to review the information on this Drafter documentation page.
0) Project Planning and Preparation
Successful programmers spend time planning before they begin coding. After reviewing the project requirements, answer the following questions to help guide your design and development process. 
What concepts from class or previous assignments might help you complete this project? Which programming concepts (loops, conditionals, lists, classes, etc.) do you expect to use? What programming skills do you want to improve while completing this project?
I plan to leverage fundamental programming concepts including loops, conditionals, and lists. Utilizing structural patterns like find, filter, map, and accumulate will help keep data processing clean and predictable. Of course I will use drafter as well.
I want to sharpen my ability to structure clean, modular Python functions with clear type hints and write robust test functions with assert_equal coverage.



Which parts of the project do you expect to be the easiest for you? The hardest? Why?
Setting up the foundational layout, creating basic user interface components (like input textboxes and display fields), and writing standard utility functions using accumulator or mapping loops.
Managing complex, mutable state across multiple interactive routes or screens, and ensuring that user inputs update the application state without introducing unexpected synchronization bugs or edge cases.





Even though you have not yet designed the final project, estimate which tasks will likely require the most time and effort? Which features or components should be implemented first? 
Most Time-Consuming: Designing the core backend logic and managing state synchronization will likely require the most careful debugging and iteration.
Core Logic: Build and thoroughly test the underlying Python functions and data structures independently.
Basic UI Integration: Wire up the primary user interface elements to the core functions.
Refinement & Testing: Make sure it looks good.



What distractions might interfere with your work and how will you minimize them? What resources will you need available while working? What questions, if any, do you still have about the assignment requirements? 
Minimizing Distractions: Background notifications and unnecessary browser tabs are the primary hurdles.
Required Resources: Python environment and documentation, course curriculum guides, and a LLM to help me with the code.



1) Site Diagram
Create a mock-up of your planned website. We suggest you make the mockup on paper, although you can also use software like PowerPoint or Slides to make a mockup. There is other design software that could also be used, but we strongly encourage you to keep it simple. Do not spend more than 15-30 minutes detailing the mock-up. Your goal should be to make a very quick and dirty diagram, to show that you have some kind of idea.


We recommend drawing each page as a rectangle, and laying out the text, buttons, and other components inside. Then, use arrows to indicate links between pages. Label each page the way you will name each function, and then put labels on the arrows to indicate what the button links. Also write down any parameters that should come into the pages.


In addition to the pages and routes, write down what fields your `State` will have, both their names and types. Think clearly about what data will need to be persistent across the entire website.


Add photo(s) or screenshot(s) of your website mock-up and labeled diagram on the next page. 

 2) Implementing Requirements
This table should serve as a draft for how you will implement the requirements into your final project. You may change your ideas later on, but your final site must fulfill all the requirements.


Requirement
Implementation
Purpose/Functionality


A 1-2 sentence description of the purpose or functionality of your site
A web application that allows a user to configure and simulate a 2D projectile motion, including a live simulation view and a post-flight analysis with a detailed flight path summary 
State Dataclass Attributes
 
Minimum of 4 attributes, one of which must be a list/dict of instances of your second dataclass.


Briefly describe each attribute, its type, and how it will be meaningfully modified throughout the site.
• initial_velocity: float: Stores the user-defined launch velocity, updated via number input in setup.
• launch_angle: float: Stores the user-defined launch angle, updated via number input in setup.
• current_time: float: Tracks the elapsed time in seconds during the live simulation.
• velocity_data: list[TrajectoryPoint] (Second Dataclass): A list storing instances of TrajectoryPoint to maintain a persistent history of coordinates and velocity components for the final analysis page.
• height_data: list[float]: A list of past calculated vertical positions used to calculate peak height or detect ground impact.
• is_running: bool: A flag that dictates whether the simulation loop is actively running or has been stopped/reset.
Second Dataclass


Your second dataclass, including its attributes, their types, and how they will be meaningfully modified (if they are modified)
TrajectoryPoint
• time_step: float: The simulation time for this point.
• x_pos: float: The calculated horizontal position.
• y_pos: float: The calculated vertical position.
• velocity_x: float: The calculated horizontal velocity component.
• velocity_y: float: The calculated vertical velocity component.
Modification: New instances are dynamically created and appended to the velocity_data list during the simulation loop whenever an update button or a timed step occurs.
Routes (minimum 7) 


The names of your route functions
1. setup_page
2. start_simulation_route
3. main_simulator_page
4. fire_action_step_route
5. reset_action_route
6. analysis_page
7. return_to_setup_route
Pages (minimum 5)


A brief description of the pages in your site
1. Setup Page: A configuration screen to enter launch velocity and angle with a 'Start' button.
2. Simulator Page: An interactive dashboard showing a live graph, a time dial, and action buttons.
3. Trajectory History Page: A detailed sub-page focusing on the persistent list of past points.
4. Analysis Page: A final summary screen displaying peak metrics, impact point, and a flight path log.
5. Error/Reset Page: A dedicated route for handling input errors or confirming a reset.
User Input (minimum 3)


Description of user input components (TextBox, TextArea, CheckBox, or SelectBox) and their purposes


For more information on these input types, see Drafter Documentation.
1. TextBox: Used on the setup page to precisely enter numerical values for initial velocity and launch angle.
2. SelectBox: Used on the main simulator or analysis page to choose from preset configurations.
3. CheckBox: Used on the simulator page to toggle the display of additional data features, such as velocity vectors or grid lines on the graph.
If Statements (minimum 3)
Brief description of what will be evaluated in your if statements and how they will meaningfully change the logic of the site
1. Evaluates if the current height state.y_pos <= 0 AND the simulation is in motion (is_running), triggering a detection of ground impact to stop the loop.
2. Evaluates if the user's angle TextBox input is outside the valid range (e.g., < 0 or > 90), changing the site logic to display an error page instead of proceeding to the simulator.
3. Evaluates if the total number of recorded TrajectoryPoint instances exceeds a maximum limit, meaningfully preventing memory issues by capping the list size.
Loop (minimum 1)
This loop must iterate over the list/dict of dataclass instances in your State attribute.
Description of this loop and why it is meaningful to the site
Iterates over the velocity_data list of TrajectoryPoint instances on the analysis page to dynamically render each past data point into a detailed table or a secondary graph displaying the specific values for each step. 

LLM Conversation
If you used an LLM in any part of this work, copy and paste every part of that conversation below. Otherwise, you may be given a zero for the assignment. Obviously, these words will not all be yours, and this is the exception to the requirement at the top of this assignment that all responses be in your own words. If you did not use an LLM to assist you in this assignment, simply say so below.
None

Final Submission
When you are finished, download this file as a Word Document (docx) and upload the file to the appropriate assignment on Canvas.




Final Project: Pick a Project
Computer Science - Week 10
Oct 3, 2026 - Version 0.0.2
Please make sure to your UD email AND name is below. Unless your UD emails are included in this table, then you will not earn any points for this assignment when it is graded! Every person should submit their own individual worksheet.

Talk about each of the questions with a friend or our LLM (or both), but make sure the words you enter below are yours (with the obvious exceptions notwithstanding). Brainstorming is best done in full sentences, and the main goal here is brainstorming. It's worth reviewing the information in this series of pages in the Drafter documentation to gain a better understanding of the process.

Role
Name
Email
Developer (You)
James Locke
zipper@udel.edu
Friend (optional)
Benjamin Louis
louisben@udel.edu


Part 1: The Goal & Prior Implementations
Identify the Goal: What specific goal are you trying to address? Think about your passions, hobbies, and academic interests. The latter are an excellent candidate to focus on. Some majors have suggestions listed below: these were provided by faculty in those departments. Other majors could consider a focus tied to a big final assignment in one of their recent courses in their major. 
Biomedical Engineering majors may consider one of the following: 
If you have started (or completed) the Cell/Tissue Design final project in BMEG100, design an organoid, which involves combining a cell type, biomaterial, and testing method. Have the website include a description and diagram of your design concept, a testing method, a needs statement, and an impact statement relevant to their organoid. Also include a link to a paper that supports your idea and a paragraph describing how that paper supports your design concept.
Otherwise, create a website related to your BMEG100 Lab Report 1, Cytoskeletal and Nuclear Staining Lab Report Guidelines, linked here (University of Delaware account required to access).
Chemistry and Chemical Engineering majors may consider creating an automated chemistry assistant that takes balanced reaction equations, starting reactant masses, and a harvested product amount to determine the limiting reactant, theoretical yield, and percent yield based on principles from Chemistry 2e (OpenStax) — Chapter 4: Chemical Reactions and Stoichiometry. To avoid manually compiling atomic mass tables or writing custom string tokenizers, use the ChemPy library to parse molecular formulas into exact molecular weights and verify reaction stoichiometry against compound data from the NIH PubChem Database. The program outputs an organized breakdown of limiting reagent status, product yields, and remaining masses of unreacted species. Also use the heat of the reaction to determine if it is exothermic or endothermic, and compute the heat flow per mole of the product.
Majors in the Electric & Computer Engineering department may consider a steganography project that hides messages in images, and then retrieves those messages from uploaded images. 
Mechanical Engineering majors may consider a project that somehow uses both the NumPy and SciPy Python libraries. 
Using both numpy and scipy, I want to build a simulation tool for 2d projectiles trajectory.


Prior Implementations: Search the internet. What existing tools or websites currently attempt to address it?
There are a lot of tools/websites like unity that can simulate 2d projectiles.


Your Implementation: Briefly describe the legitimate purpose or functionality of your site. How would you want this web application to be used?
This would be an educational tool that allows students and instructors to simulate 2d projectile motion under realistic atmospheric drag forces.  Users can adjust physical parameters such as launch angle, velocity, mass, and drag coefficient.  These allow the user to analyze real-time trajectory curves and compare ideal vs drag dynamics.  


Part 2: The Input-Process-Output (IPO) Model
Think about the fundamental flow of your program.
The Core Goal: Every program has three main phases: taking input, processing data, and presenting output. In one sentence, what is the ultimate goal your program will accomplish for the user? Be specific and use CS1 concepts.
The program takes user-defined projectile parameters as input, processes them by numerically integrating differential equations with NumPy array state vectors, and outputs the resulting trajectory coordinates as an interactive graph and telemetry display. 



Input: What specific information will the user need to provide to your program? (e.g., a city name, a numerical budget, a list of hobbies).
The user will need to provide initial physical parameters, including initial launch velocity, launch angle, projectile mass, cross-sectional area, drag coefficient, and environmental fluid density. 



Processing: At a high level, how will the computer manipulate or evaluate that data? (e.g., calculate the average, filter out options that are too expensive, compare the input against a database).
The computer will process the inputs by using NumPy arrays to set up the projectile's equations of motion and SciPy's solve_ivp to integrate them over time, calculating the position and velocity at each timestep. 



Output: What will the user get back? (e.g., a recommendation, a calculated safety factor, a formatted schedule).
The user will get back an interactive trajectory plot comparing ideal versus drag motion, alongside a telemetry dashboard displaying key metrics like total range, max altitude, flight time, and final impact velocity. 



Part 3: Data Abstraction
Identify the "nouns" of your problem.
Representing Reality: Abstraction is the process of representing the real world inside a computer by ignoring unnecessary details. What are the core "things" (nouns) your program needs to track? (e.g., If building a recipe app, the nouns are "Recipe" and "Ingredient").
Projectile(thing being launched), Environment(conditions of the launch), Trajectory Point(the state of a projectile at a given time), Simulation Report(complete collection of output data).



Identifying Properties: For the most important "thing" you listed above, what 3 to 4 specific details do you actually need to solve your problem, and what details will you abstract away?
Details I need: (e.g., Ingredient name, weight, cost)
Details I will ignore: (e.g., Ingredient color, brand, expiration date)
Need: Mass, Radius, Drag Coefficient, Initial Velocity

Ignore: Color/Texture, Material Composition, Spin, Shape Change


Part 4: Challenges, AI Strategy, & Goals
Difficulties: What parts of this project seem the most difficult or technically complex?
Getting the drag physics correct.  Integrating drafter.  Data Processing using SciPy.


Coding Strategy: If you will be using an LLM to help code, how will you ensure you understand the generated code and avoid "hallucinations" or "shallow learning" (copying without understanding)? If you won't be using an LLM to help code, this project might take about 4 hours a week to complete, so list each of the days and times in which you work on the project. 
I will take a small chunk of code and review it, to make sure it is correct and I understand it.  I will also make the LLM use more things I am aware of, even if it will be longer code.


Goals: What is your ultimate goal for this project? (e.g., Impress the graders with a creative UI, build something I can use in my other classes, learn Drafter deeply).
I want to learn how to use SciPy and NumPy for future use.  I want to make something that impresses me, by seeing how much I’ve learned.


Part 5: Research & Brainstorming Conversation
Have a conversation with a Generative AI tool (like ChatGPT or Claude) OR a friend about your project idea. Do not ask for code. Instead, use the AI/friend as a sounding board to research your problem.
The Initial Prompt/Question: Ask the AI or your friend to help you brainstorm. (e.g., "I want to build a simple web tool to help students track their study hours. What are 3 common problems students face when tracking their time, and what are 3 simple features a basic tool should have?"). Paste your prompt below:
I want to build a web-based 2D projectile motion simulator in Python using Drafter and SciPy. What are 3 core interactive features that would make this tool helpful for physics students, and what is one advanced feature I could consider adding? 



The Response: Briefly summarize the best ideas the AI or your friend suggested. What existing solutions or prior apps did they mention?
Key Features:
Sliders for launch angle, initial velocity, mass, and drag coefficient.
A plotted trajectory canvas along with numerical outputs for peak height, total flight time, and horizontal range.
Buttons for common launch environments (Earth gravity vs. Moon gravity, or vacuum vs. high-drag air).
Advanced Features & Apps:
3D spin dynamics, and an interactive 3D particle rendering canvas.
PhET Interactive Simulations and Desmos Graphing Calculator.





The Pushback: You must reply to the AI/friend to narrow the scope when it's over-ambitious. Pick the most complex feature they suggested and explain why it is too complicated for an  introductory programming project. Ask them for a simpler alternative. Paste your response here:
Implementing 3D rotational vector calculus and web-based 3D rendering adds unnecessary technical bloat. Can you suggest a much simpler alternative feature that still enhances student learning within a 2D state model? 



Reflection: Based on this conversation, how has your project idea changed or become more focused?
The project stays strictly bound to a 2D point-mass particle model.

Instead of complex 3D graphics, the simpler alternative decided on is a Side-by-Side Trajectory Comparison (comparing a projectile launched with air resistance against one without air resistance on the same 2D plot).


Part 6: Resource Planning
What resources will you use if you get stuck? 
I will use office hours and LLM’s if I get stuck.


If your LLM provides code that causes a Drafter or Bakery error, or if you run into a problem during deployment, what is your step-by-step debugging plan to resolve it?
First, find out where the code failed.  Next, deconstruct any complex or generated code into smaller helper functions.  From there, write unit tests.  



Part 7: LLM Conversation
If you used an LLM in any part of this work, copy and paste every part of that conversation below. Otherwise, you may be given a zero for the assignment. Obviously, these words will not all be yours, and this is the exception to the requirement at the top of this assignment that all responses be in your own words. If you did not use an LLM to assist you in this assignment, simply say so below.
Me:
I want to build a web-based 2D projectile motion simulator in Python using Drafter and SciPy. What are 3 core interactive features that would make this tool helpful for physics students, and what is one advanced feature I could consider adding? 

LLM:
Key Features Suggested:
Interactive Controls: Sliders/inputs for launch angle, initial velocity, mass, and drag coefficient.
Trajectory Visualization & Metrics: A plotted trajectory canvas along with numerical outputs for peak height, total flight time, and horizontal range.
Preset Scenarios: Pre-configured buttons for common launch environments (e.g., Earth gravity vs. Moon gravity, or vacuum vs. high-drag air).
Advanced Features & Prior Apps Mentioned:
Suggested Advanced Feature: Real-time multi-body orbital mechanics, 3D spin dynamics (Magnus effect), and an interactive 3D particle rendering canvas.
Prior Apps Mentioned: PhET Interactive Simulations (Projectile Motion by University of Colorado Boulder) and Desmos Graphing Calculator.
Me:
Implementing 3D rotational vector calculus and web-based 3D rendering adds unnecessary technical bloat. Can you suggest a much simpler alternative feature that still enhances student learning within a 2D state model? 

LLM:
Here are three simple, highly educational 2D features that avoid unnecessary technical complexity while enhancing student learning:
Dual-Trajectory Overlay (Vacuum vs. Air Resistance)
How it works: Plot two trajectories simultaneously on the same 2D axes: an ideal theoretical parabolic arc (Cd=0) and a realistic trajectory that incorporates quadratic drag (Fdv2).
Educational Value: Visually demonstrates the exact impact of atmospheric drag on launch range, peak height, and flight symmetry without changing the underlying 2D coordinate system.
Preset Environment & Launch Targets
How it works: Include standard preset buttons for different environments (e.g., Earth gravity vs. Moon/Mars gravity, or dense air vs. high altitude) alongside a target horizontal distance on the ground plane.
Educational Value: Allows students to explore how gravitational acceleration (g) and fluid density () alter kinetic outcomes, turning the simulator into a goal-oriented problem-solving tool.
Key Trajectory Snapshot Metrics
How it works: Compute and display a small, structured panel of scalar outputs alongside the 2D curve, such as maximum height (ymax), total time of flight (tfinal), impact velocity magnitude (vfinal), and the launch angle for maximum range under drag.
Educational Value: Gives students instant feedback to compare against hand-calculated kinematic equations, emphasizing how non-linear air resistance breaks standard symmetrical rules (like 45 yielding maximum range).




Part 8: Submit
In Google docs, with this document open, please click on File > Download > Microsoft Word (.docx), and make sure you put that download somewhere you can find it again. Then, upload it to the Canvas assignment about selecting or brainstorming your final project. 

When you're done with this assignment, review this page of the Drafter documentation to better prepare for the next step.
