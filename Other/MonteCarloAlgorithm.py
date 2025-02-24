import random
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    inside_circle = 0
    points_inside = []
    points_outside = []

    for _ in range(num_points):
        x, y = random.uniform(-2, 2), random.uniform(-2, 2)
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 4:
            inside_circle += 1
            points_inside.append((x, y))
        else:
            points_outside.append((x, y))

    # Ratio of points inside circle to total points approximates pi/4
    pi_estimate = 4 * (inside_circle / num_points)
    return pi_estimate, points_inside, points_outside

def visualize(points_inside, points_outside):
    plt.figure(figsize=(8, 8))
    
    # Plot points inside the circle
    if points_inside:
        inside_x, inside_y = zip(*points_inside)
        plt.scatter(inside_x, inside_y, color='blue', s=1, label='Inside Circle')

    # Plot points outside the circle
    if points_outside:
        outside_x, outside_y = zip(*points_outside)
        plt.scatter(outside_x, outside_y, color='red', s=1, label='Outside Circle')

    # Draw the unit circle
    circle = plt.Circle((0, 0), 2, color='black', fill=False, linewidth=1.5, label='Unit Circle')
    plt.gca().add_artist(circle)

    # Formatting
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Monte Carlo Simulation for Estimating Pi')
    plt.show()

if __name__ == "__main__":
    try:
        num_points = 20000  # Predefined value for sandbox environments
        pi_estimate, points_inside, points_outside = estimate_pi(num_points)
        print(f"Estimated value of pi using {num_points} points: {pi_estimate}")
        visualize(points_inside, points_outside)
    except Exception as e:
        print(f"An error occurred: {e}")


