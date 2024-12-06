import os
import re

def get_lines_from_file(file_name, single_line=False):
    try:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return ''.join(lines) if single_line else lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def main():
    line = get_lines_from_file("input.txt", single_line=True)

    tokens = re.findall(r"mul\(\d+,\d+\)", line)

    sum = 0
    for token in tokens:
        x, y = token[4:len(token)-1].split(",")

        if(not x.isdigit() or not y.isdigit()):
            continue

        sum += int(x) * int(y)

    print(f"sum: {sum}")

if __name__ == "__main__":
    main()