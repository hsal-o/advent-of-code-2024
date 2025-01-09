import os
import time
from enum import Enum

class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)

    @classmethod
    def rotate(self, current):
        directions = list(self)
        index = directions.index(current)
        return directions[(index + 1) % len(directions)]

def get_lines_from_file(file_name, single_line=False):
    try:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line.replace('\n', '') for line in lines]
        return ''.join(lines) if single_line else lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def get_start_pos(grid):
    for y, row in enumerate(grid):
        x = row.find("^")
        if(x != -1):
            return (y, x)

def count_guard_steps(grid):
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    steps = set([])
    curr_y, curr_x = get_start_pos(grid)
    steps.add((curr_x, curr_y))

    curr_dir = Direction.NORTH
    while(True):
        dy, dx = curr_dir.value         
        ny = curr_y + dy
        nx = curr_x + dx

        # Check if next step leaves grid
        if(ny < 0 or ny >= HEIGHT or nx < 0 or nx >= WIDTH):
            break

        # Check if next step would bump into obstacle
        if(grid[ny][nx] == "#"):
            curr_dir = Direction.rotate(curr_dir)
            continue
        
        # Valid step
        curr_y = ny
        curr_x = nx
        steps.add((curr_x, curr_y))

    return len(steps)

def main():
    grid = get_lines_from_file("input.txt")
   
    print(f"count: {count_guard_steps(grid)}")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"elapsed time: {(time.time() - start):.4f} seconds")