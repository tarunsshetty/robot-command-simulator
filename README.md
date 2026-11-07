# Robot Command Simulator

A small Python program I wrote where you control a robot on a 10x10 grid
from the terminal. The robot is shown as `@`, and the grid is printed again
after every command so you can see where it went.

## Commands

- `F` moves the robot one step forward
- `L` turns it left
- `R` turns it right
- `Q` quits

Lowercase works too, so `f` is the same as `F`. The robot starts at (0, 0)
facing north. If it tries to walk off the grid, it just stays where it is
and prints "Wall ahead!".

## Running it

You only need Python 3.

```
git clone https://github.com/<your-username>/robot-command-simulator.git
cd robot-command-simulator
python robot_simulator.py
```

## Sample run

```
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
@ . . . . . . . . .
Position: 0 0  Facing: N

Command: F
```

## How it works

The robot's position is stored in `x` and `y`, and its direction in `facing`.
For turning, I keep the directions in a list (`N, E, S, W`) and move the
index up or down by one. The `% 4` makes it wrap around, so turning left
from north goes to west.

For moving, I first work out the new position and only update `x` and `y`
if it is still inside the grid. That is how the wall check works.

## What I'd like to add next

Obstacles, and reading a whole command string like `FFRFFL` from a file
instead of typing one command at a time.

## Author
Tarun.S.Shetty
