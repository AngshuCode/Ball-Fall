import time
import math

def calculate_position(initial_height, time_elapsed, gravity):
  """Calculates the position of the ball at a given time."""
  position = initial_height - 0.5 * gravity * time_elapsed**2
  return max(0, position) # Ensure the ball doesn't go below the ground

def calculate_fall_time(initial_height, gravity):
  """Calculates the total fall time."""
  if initial_height < 0:
    return 0
  return math.sqrt(2 * initial_height / gravity)

def drop_ball(ball_number, initial_height, gravity):
  """Simulates a single ball falling and calculates fall time."""
  print(f"\nDropping Ball {ball_number} from a height of {initial_height:.2f} meters...")
  time_elapsed = 0
  while True:
    position = calculate_position(initial_height, time_elapsed, gravity)
    print(f"Time: {time_elapsed:.2f}s, Height: {position:.2f}m", end='\r')
    if position <= 0:
      print(f"\nBall {ball_number} hit the ground!")
      fall_time = calculate_fall_time(initial_height, gravity)
      print(f"Total fall time for Ball {ball_number}: {fall_time:.2f} seconds")
      break
    time.sleep(0.1)  # Introduce a small delay for visualization
    time_elapsed += 0.1

def main():
  """Allows the user to drop single or multiple balls."""
  kolkata_gravity = 9.79  # Acceleration due to gravity in Kolkata (approx.)
  while True:
    try:
      num_balls = int(input("Enter the number of balls to drop (or 0 to quit): "))
      if num_balls <= 0:
        print("Exiting simulation.")
        break
      initial_height = float(input("Enter the initial height (in meters): "))
      for i in range(1, num_balls + 1):
        drop_ball(i, initial_height, kolkata_gravity)
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()