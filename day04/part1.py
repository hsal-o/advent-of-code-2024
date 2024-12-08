import os
import time

DIRECTIONS = [
    (-1, 0),  # North
    (1, 0),   # South
    (0, -1),  # West
    (0, 1),   # East
    (-1, -1), # Northwest
    (-1, 1),  # Northeast
    (1, -1),  # Southwest
    (1, 1)    # Southeast
]

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
    
def find_word(grid, start_row, start_col, delta_row, delta_col, word):
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    for i, char in enumerate(word):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        
        if(row < 0 or row >= num_rows) or (col < 0 or col >= num_cols):
            return False
        
        if grid[row][col] != char:
            return False
        
    return True

def main():    
    lines = get_lines_from_file("input.txt")
    
    word = "XMAS"
    num_rows = len(lines)
    num_cols = len(lines[0])
    count = 0
    
    for row in range(num_rows):
        for col in range(num_cols):
            for delta_row, delta_col in DIRECTIONS:
                if find_word(lines, row, col, delta_row, delta_col, word):
                    count += 1
    
    print(f"count: {count}")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"elapsed time: {(time.time() - start):.4f} seconds")