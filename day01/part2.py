def get_lines_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return lines
    except Exception:
        print(f"File '{file_name}' not found")
        return None
    
def main():
    lines = get_lines_from_file("input.txt")

    left = []
    right = {}
    for line in lines:
        l, r = [int(part) for part in line.split() if part.isdigit()]
        left.append(l)
        right[r] = right[r] + 1 if (r in right) else 1

    sum = 0
    for i in range(len(left)):
        num = left[i]
        if num in right:
            sum += num * right[num]

    print(f"sum: {sum}")

if __name__ == "__main__":
    main()