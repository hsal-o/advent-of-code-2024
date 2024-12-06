def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def is_safe(line):
    line = [int(x) for x in line.split()]

    is_increasing = line[1] - line[0] > 0

    for i in range(len(line) - 1):
        if (line[i+1] == line[i]):
            return False

        # Check for inconsistent ordering
        if (line[i+1] - line[i] > 0) != is_increasing:
            return False
        
        dif = abs(line[i+1] - line[i])
        if not (dif >= 1 and dif <= 3):
            return False
    
    return True
    
def main():
    lines = get_lines_from_file("input.txt")

    count = 0
    for line in lines:
        count += 1 if is_safe(line) else 0

    print(f"count: {count}")
 

if __name__ == "__main__":
    main()