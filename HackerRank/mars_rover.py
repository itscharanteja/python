def rover_move(matrix_size, cmds):
    result = 0
    for cmd in cmds:
        result = process(cmd, matrix_size, result)
    return result

def process(cmd, n, current):
    if cmd == "DOWN":
        if current < (n * n) - n:
            current += n
    elif cmd == "UP":
        if current >= n:
            current -= n
    elif cmd == "RIGHT":
        if (current + 1) % n != 0:
            current += 1
    elif cmd == "LEFT":
        if current % n != 0:
            current -= 1
    return current

if __name__ == "__main__":
    l = ["RIGHT", "RIGHT", "DOWN"]
    rover_move_result = rover_move(4, l)
    print(rover_move_result)
