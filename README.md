# robot-command-simulator
A small Python project where I control a robot on a 10x10 grid using text commands like forward, left and right.
Robot Command Simulator

This is a small Python program where I move a robot around a 10x10 grid by typing commands. I made it to practice Python and to see how a program can take instructions one at a time.

The robot starts at the bottom left corner facing north. You type F to move forward, L to turn left, R to turn right and Q to quit. After every command the grid is printed again with the robot shown as @.

If the robot is at the edge and you tell it to go forward, it says "Wall ahead" and stays where it is.

To run it, install Python and type this in the terminal:

    python robot_commands.py

The hardest part for me was the turning. I had to find a way to go from W back to N, and I used a list of directions with % 4 to do it.

Right now it is very basic. Next I want to add walls inside the grid, a goal cell, and a way to type many commands at once like FFRFF.
