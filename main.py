from drafter import *
from dataclasses import dataclass
import matplotlib.pyplot as plt
import math

@dataclass
class TrajectoryPoint:
    """Represents a single calculated point along the projectile path."""
    time_step: float
    x_pos: float
    y_pos: float
    velocity_x: float
    velocity_y: float

@dataclass
class State:
    """The current state of the 2D Projectile Motion Simulator application."""
    initial_velocity: float
    launch_angle: float
    current_time: float
    current_x: float
    current_y: float
    is_running: bool
    gravity: float
    trajectory_data: list[TrajectoryPoint]
    status_message: str

def calculate_step(velocity: float, angle: float, gravity: float, t: float) -> TrajectoryPoint:
    """Calculates position and velocity components at time t."""
    rad = math.radians(angle)
    v0x = velocity * math.cos(rad)
    v0y = velocity * math.sin(rad)
    
    x = v0x * t
    y = (v0y * t) - (0.5 * gravity * (t ** 2))
    vx = v0x
    vy = v0y - (gravity * t)
    
    return TrajectoryPoint(
        time_step=round(t, 2),
        x_pos=round(x, 2),
        y_pos=round(max(0.0, y), 2),
        velocity_x=round(vx, 2),
        velocity_y=round(vy, 2)
    )

def build_arch_plot(state: State) -> MatPlotLibPlot:
    """Generates a matplotlib parabolic arch showing the full path and current object position."""
    plt.figure(figsize=(6, 4))
    
    # 1. Calculate the full theoretical arch (dashed guide curve)
    rad = math.radians(state.launch_angle)
    v0x = state.initial_velocity * math.cos(rad)
    v0y = state.initial_velocity * math.sin(rad)
    total_flight_time = (2 * v0y) / state.gravity if state.gravity > 0 else 1.0
    if total_flight_time <= 0:
        total_flight_time = 1.0
    
    guide_x = []
    guide_y = []
    steps = 50
    for i in range(steps + 1):
        t = (total_flight_time * i) / steps
        guide_x.append(v0x * t)
        guide_y.append(max(0.0, (v0y * t) - (0.5 * state.gravity * (t ** 2))))
        
    plt.plot(guide_x, guide_y, linestyle="--", color="gray", alpha=0.6, label="Predicted Arch")
    
    # 2. Plot the actual recorded steps traveled so far
    if state.trajectory_data:
        traveled_x = [pt.x_pos for pt in state.trajectory_data]
        traveled_y = [pt.y_pos for pt in state.trajectory_data]
        plt.plot(traveled_x, traveled_y, marker="o", linestyle="-", color="royalblue", label="Path Traveled")
    
    # 3. Highlight the projectile's current position
    plt.plot([state.current_x], [state.current_y], marker="o", markersize=12, color="crimson", label="Projectile")
    
    plt.title(f"Projectile Motion Arch (v0={state.initial_velocity} m/s, θ={state.launch_angle}°)")
    plt.xlabel("Horizontal Distance X (m)")
    plt.ylabel("Vertical Height Y (m)")
    plt.ylim(bottom=0)
    plt.xlim(left=0)
    plt.grid(True, linestyle=":", alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    # Return plot component (Do not call plt.close() here so Drafter can render it)
    return MatPlotLibPlot()

# ==========================================
# MAIN INDEX & ROUTES
# ==========================================

@route
def index(state: State) -> Page:
    """Default entry point for Drafter: Renders the initial setup page."""
    return Page(
        state,
        [
            Header("2D Projectile Simulator - Setup"),
            state.status_message,
            "Initial Velocity (m/s):",
            TextBox("velocity_input", str(state.initial_velocity)),
            "Launch Angle (degrees):",
            TextBox("angle_input", str(state.launch_angle)),
            Button("Start Simulation", "start_simulation"),
        ]
    )

@route
def start_simulation(state: State, velocity_input: str, angle_input: str) -> Page:
    """Validates inputs, initializes physics state, and moves to simulator page."""
    try:
        v = float(velocity_input)
        a = float(angle_input)
        
        if v <= 0 or a < 0 or a > 90:
            state.status_message = "Error: Velocity must be > 0 and angle between 0 and 90."
            return index(state)
            
        state.initial_velocity = v
        state.launch_angle = a
        state.current_time = 0.0
        state.is_running = True
        state.trajectory_data = []
        
        initial_point = calculate_step(v, a, state.gravity, 0.0)
        state.trajectory_data.append(initial_point)
        state.current_x = initial_point.x_pos
        state.current_y = initial_point.y_pos
        state.status_message = "Simulation started successfully!"
        
        return simulator_page(state)
    except ValueError:
        state.status_message = "Error: Please enter valid numbers."
        return index(state)

@route
def simulator_page(state: State) -> Page:
    """Renders the main interactive simulator dashboard."""
    status = "In Flight" if state.is_running else "Grounded / Stopped"
    return Page(
        state,
        [
            Header("2D Projectile Simulator - Dashboard"),
            state.status_message,
            f"Status: {status}",
            f"Current Time: {state.current_time}s",
            f"Position: X={state.current_x}m, Y={state.current_y}m",
            Button("Fire Step (+1s)", "fire_step"),
            Button("View Trajectory Arch", "trajectory_page"),
            Button("View History Log", "history_page"),
            Button("View Flight Analysis", "analysis_page"),
            Button("Reset Simulation", "reset_simulation"),
        ]
    )

def advance_one_second(state: State) -> None:
    """Helper to step the physics forward by 1 second."""
    if state.is_running:
        state.current_time += 1.0
        new_point = calculate_step(state.initial_velocity, state.launch_angle, state.gravity, state.current_time)
        
        if new_point.y_pos <= 0.0:
            new_point.y_pos = 0.0
            state.is_running = False
            state.status_message = "Projectile landed!"
        else:
            state.status_message = f"Advanced to t={state.current_time}s"
            
        state.trajectory_data.append(new_point)
        state.current_x = new_point.x_pos
        state.current_y = new_point.y_pos

@route
def fire_step(state: State) -> Page:
    """Advances simulation time step by 1 second from the dashboard."""
    advance_one_second(state)
    return simulator_page(state)

@route
def fire_step_on_arch(state: State) -> Page:
    """Advances simulation time step by 1 second directly on the visual arch screen."""
    advance_one_second(state)
    return trajectory_page(state)

@route
def trajectory_page(state: State) -> Page:
    """Renders the visual parabolic arch screen showing the object in motion."""
    status = "In Flight" if state.is_running else "Grounded / Stopped"
    arch_graph = build_arch_plot(state)
    
    return Page(
        state,
        [
            Header("Trajectory Motion Arch"),
            state.status_message,
            f"Status: {status} | Time: {state.current_time}s | Position: ({state.current_x}m, {state.current_y}m)",
            arch_graph,
            Button("Step Forward (+1s)", "fire_step_on_arch"),
            Button("Back to Dashboard", "simulator_page"),
            Button("View Flight Analysis", "analysis_page"),
        ]
    )

@route
def reset_simulation(state: State) -> Page:
    """Resets the simulation parameters back to setup (index)."""
    state.current_time = 0.0
    state.current_x = 0.0
    state.current_y = 0.0
    state.is_running = False
    state.trajectory_data = []
    state.status_message = "Simulation reset."
    return index(state)

@route
def history_page(state: State) -> Page:
    """Renders the history log page iterating over trajectory data instances."""
    content = [
        Header("Trajectory Point History Log"),
        state.status_message,
    ]
    
    for pt in state.trajectory_data:
        log_entry = f"Time: {pt.time_step}s | Pos: ({pt.x_pos}m, {pt.y_pos}m) | Vel: ({pt.velocity_x}, {pt.velocity_y})"
        content.append(log_entry)
        
    content.append(Button("Back to Dashboard", "simulator_page"))
    return Page(state, content)

@route
def analysis_page(state: State) -> Page:
    """Renders the final flight summary and analysis."""
    max_h = max([p.y_pos for p in state.trajectory_data]) if state.trajectory_data else 0.0
    total_d = state.trajectory_data[-1].x_pos if state.trajectory_data else 0.0
    
    return Page(
        state,
        [
            Header("Flight Analysis & Summary"),
            state.status_message,
            f"Peak Height: {max_h} meters",
            f"Total Distance: {total_d} meters",
            f"Total Points Recorded: {len(state.trajectory_data)}",
            Button("View Trajectory Arch", "trajectory_page"),
            Button("Back to Dashboard", "simulator_page"),
            Button("Start Over", "reset_simulation"),
        ]
    )

# ==========================================
# SERVER START & TESTS
# ==========================================

initial_test_state = State(50.0, 45.0, 0.0, 0.0, 0.0, False, 9.81, [], "Configure your launch.")

assert_equal(
    index(initial_test_state),
    Page(
        initial_test_state,
        [
            Header("2D Projectile Simulator - Setup"),
            "Configure your launch.",
            "Initial Velocity (m/s):",
            TextBox("velocity_input", "50.0"),
            "Launch Angle (degrees):",
            TextBox("angle_input", "45.0"),
            Button("Start Simulation", "start_simulation"),
        ]
    )
)

start_server(initial_test_state)
