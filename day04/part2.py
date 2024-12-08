import os
import re
import time

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
    
def main():
    lines = get_lines_from_file("input.txt", )

    num_rows = len(lines)
    num_cols = len(lines[0])

    count = 0
    for row in range(1, num_rows-1):
        for col in range(1, num_cols-1):
            if lines[row][col] != 'A':
                continue
            
            top_left = lines[row-1][col-1]
            top_right = lines[row-1][col+1]
            bot_left = lines[row+1][col-1] 
            bot_right = lines[row+1][col+1]
            if (
                ((top_left == 'M' and bot_right == 'S') or (top_left == 'S' and bot_right == 'M'))
                and
                ((bot_left == 'M' and top_right == 'S') or (bot_left == 'S' and top_right == 'M'))
            ):
                count += 1

    print(f"count: {count}")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"elapsed time: {(time.time() - start):.4f} seconds")