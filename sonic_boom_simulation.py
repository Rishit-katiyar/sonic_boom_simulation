import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate pressure disturbance at each point
def calculate_pressure_distribution(X, Y, t, source_position, speed_of_propagation):
    # Calculate distance from the source
    distance_from_source = np.sqrt((X - source_position[0])**2 + (Y - source_position[1])**2)
    # Calculate pressure distribution
    pressure = np.zeros_like(distance_from_source)
    pressure[distance_from_source <= speed_of_propagation * t] = 1  # Wavefront
    return pressure

# Function to generate animation frames
def generate_animation_frames(X, Y, time_steps, source_position, speed_of_propagation):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create animation frames
    for t in time_steps:
        # Calculate pressure distribution for current time step
        Z = calculate_pressure_distribution(X, Y, t, source_position, speed_of_propagation)

        # Create a 3D surface plot
        ax.clear()
        ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

        # Add contours to show shock wave fronts
        ax.contour(X, Y, Z, zdir='z', offset=-0.5, cmap='viridis', linewidths=1)

        # Set axis limits and labels
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-0.5, 1)
        ax.set_xlabel('Distance (X)')
        ax.set_ylabel('Distance (Y)')
        ax.set_zlabel('Pressure')

        plt.title(f'Shock Wave Visualization (Time: {t:.2f})')
        plt.pause(0.1)  # Pause to display the plot

# Customized Parameters Mode
def customized_parameters_mode():
    # Parameters
    num_points = 100
    x = np.linspace(-1, 1, num_points)
    y = np.linspace(-1, 1, num_points)
    X, Y = np.meshgrid(x, y)

    # Default parameters
    default_source_position = (0, 0)
    default_speed_of_propagation = 0.5
    default_start_time = 0
    default_end_time = 2
    default_num_time_steps = 10
    default_time_steps = np.linspace(default_start_time, default_end_time, default_num_time_steps)

    print("Default Parameters:")
    print(f"Source Position: {default_source_position}")
    print(f"Speed of Propagation: {default_speed_of_propagation}")
    print(f"Start Time: {default_start_time}")
    print(f"End Time: {default_end_time}")
    print(f"Number of Time Steps: {default_num_time_steps}")

    # Input parameters with error handling
    try:
        source_position = tuple(map(float, input("\nEnter source position (x, y): ").split())) or default_source_position
        speed_of_propagation = float(input("Enter speed of propagation: ") or default_speed_of_propagation)
        start_time = float(input("Enter start time: ") or default_start_time)
        end_time = float(input("Enter end time: ") or default_end_time)
        num_time_steps = int(input("Enter number of time steps: ") or default_num_time_steps)
        time_steps = np.linspace(start_time, end_time, num_time_steps)
    except ValueError:
        print("Invalid input. Using default parameters instead.")
        source_position = default_source_position
        speed_of_propagation = default_speed_of_propagation
        start_time = default_start_time
        end_time = default_end_time
        num_time_steps = default_num_time_steps
        time_steps = default_time_steps

    # Generate animation frames
    generate_animation_frames(X, Y, time_steps, source_position, speed_of_propagation)

# Default Parameters Mode
def default_parameters_mode():
    # Parameters
    num_points = 100
    x = np.linspace(-1, 1, num_points)
    y = np.linspace(-1, 1, num_points)
    X, Y = np.meshgrid(x, y)

    # Default parameters
    source_position = (0, 0)
    speed_of_propagation = 0.5
    start_time = 0
    end_time = 2
    num_time_steps = 10
    time_steps = np.linspace(start_time, end_time, num_time_steps)

    print("Default Parameters:")
    print(f"Source Position: {source_position}")
    print(f"Speed of Propagation: {speed_of_propagation}")
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Number of Time Steps: {num_time_steps}")

    # Generate animation frames
    generate_animation_frames(X, Y, time_steps, source_position, speed_of_propagation)

# Main function
def main():
    mode = input("Choose mode: (1) Customized parameters (2) Default parameters: ")
    if mode == '1':
        customized_parameters_mode()
    elif mode == '2':
        default_parameters_mode()
    else:
        print("Invalid mode selection.")

# Entry point of the program
if __name__ == "__main__":
    main()
