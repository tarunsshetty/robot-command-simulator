# Robot command simulator

size = 10
x = 0
y = 0
facing = "N"
directions = ["N", "E", "S", "W"]


def show_grid():
    for row in range(size - 1, -1, -1):
        line = ""
        for col in range(size):
            if col == x and row == y:
                line += "@ "
            else:
                line += ". "
        print(line)
    print("Position:", x, y, " Facing:", facing)
    print()


print("F = forward, L = turn left, R = turn right, Q = quit")
show_grid()

while True:
    command = input("Command: ").upper()

    if command == "Q":
        print("Robot stopped.")
        break
    elif command == "L":
        facing = directions[(directions.index(facing) - 1) % 4]
    elif command == "R":
        facing = directions[(directions.index(facing) + 1) % 4]
    elif command == "F":
        new_x = x
        new_y = y
        if facing == "N":
            new_y += 1
        elif facing == "S":
            new_y -= 1
        elif facing == "E":
            new_x += 1
        elif facing == "W":
            new_x -= 1

        if 0 <= new_x < size and 0 <= new_y < size:
            x = new_x
            y = new_y
        else:
            print("Wall ahead! Robot can't move.")
    else:
        print("Unknown command")

    show_grid()