def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def is_safe(line):
    is_increasing = line[1] - line[0] > 0

    for i in range(len(line) - 1):
        if (line[i+1] == line[i]):
            return False

        if (line[i+1] - line[i] > 0) != is_increasing:
            return False
        
        dif = abs(line[i+1] - line[i])
        if not (dif >= 1 and dif <= 3):
            return False
    
    return True

def check_line_safety(line):
    if is_safe(line):
        return True
    
    for i in range(len(line)):
        new_line = line.copy()
        new_line.pop(i)
        if(is_safe(new_line)):
            return True
    return False
    
def main():
    lines = get_lines_from_file("input.txt")

    count = 0
    for line in lines:
        line = [int(x) for x in line.split()]
        if check_line_safety(line):
            count += 1

    print(f"count: {count}")
 

if __name__ == "__main__":
    main()