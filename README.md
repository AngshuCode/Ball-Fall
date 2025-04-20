# Falling Ball Simulation in Python

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ## Description

This Python program simulates the motion of one or more balls falling under the influence of gravity. It allows the user to specify the number of balls to drop and the initial height from which they are released. The simulation calculates and displays the position of each ball over time until it hits the ground, and then reports the total fall time. The program uses an approximate value for the acceleration due to gravity in Kolkata.

## Installation

No specific installation is required to run this Python script, as it uses standard Python libraries. Ensure you have Python 3 installed on your system. or ensure your pc is not a potato

1.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `falling_ball_simulation.py`).

## Usage

1.  **Open a terminal or command prompt.**
2.  **Navigate to the directory** where you saved the Python file.
3.  **Run the script** using the command:
    ```bash
    python falling_ball_simulation.py
    ```
4.  **Follow the prompts:**
    * The program will ask you to enter the number of balls you want to simulate. Enter a positive integer. To quit the program, enter `0`.
    * If you enter a positive number of balls, the program will then ask you to enter the initial height (in meters) from which the balls will be dropped. Enter a positive floating-point number.
    * The simulation will then start, showing the time elapsed and the height of each ball as it falls.
    * Once a ball hits the ground, a message will be displayed, along with the total fall time for that ball.
    * The program will then loop back to ask if you want to drop more balls.

## Code Explanation

The program consists of the following functions:

* `calculate_position(initial_height, time_elapsed, gravity)`: This function takes the initial height, the time elapsed since the ball was dropped, and the acceleration due to gravity as input. It calculates the current vertical position of the ball using the kinematic equation:
    $\qquad position = initial\_height - \frac{1}{2} g t^2$
    It ensures that the position does not go below zero (the ground).

* `calculate_fall_time(initial_height, gravity)`: This function calculates the theoretical total fall time of an object dropped from a given initial height under constant gravity, using the formula:
    $\qquad t = \sqrt{\frac{2h}{g}}$

* `drop_ball(ball_number, initial_height, gravity)`: This function simulates the fall of a single ball. It prints the ball's number and initial height, then iteratively calculates and displays its position as time progresses. When the ball reaches the ground, it prints a message and the total fall time.

* `main()`: This is the main function that controls the program flow. It sets the approximate acceleration due to gravity for Kolkata ($9.79 \, \text{m/s}^2$). It prompts the user for the number of balls and the initial height and then calls the `drop_ball` function for each ball. It includes error handling for invalid input.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. You can contribute by:

* Adding features (e.g., incorporating air resistance, different environments).
* Improving the visualization.
* Fixing bugs.
* Adding more detailed comments or documentation.

Please follow standard Python coding conventions (PEP 8).

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details. ## Author

[Angshu] ([Your GitHub Profile URL](https://github.com/AngshuCode )) ## Acknowledgments

* This simulation utilizes the fundamental principles of Newtonian mechanics.
* The approximate value for gravity in Kolkata was obtained from online resources.
