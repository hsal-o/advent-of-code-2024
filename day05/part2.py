import os
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
    
def get_data(lines):
    rules = []
    page_orders_list = []

    # Extract rules
    i = 0
    while lines[i]:
        rule = list(map(int, lines[i].split("|")))
        rules.append((rule[0], rule[1]))
        i += 1

    i += 1

    # Extract page numbers
    while i < len(lines):
        pages = list(map(int, lines[i].split(",")))

        page_order = {}
        for j in range(len(pages)):
            page_order[pages[j]] = j

        page_orders_list.append(page_order)
        i += 1

    return rules, page_orders_list

def process_page_order(page_order, rules):
    invalid = False

    i = 0
    while i < len(rules):
        x, y = rules[i]

        if(x not in page_order.keys() or y not in page_order.keys()): 
            i += 1
            continue

        if(page_order[x] > page_order[y]):
            invalid = True

            # Swap values
            tmp = page_order[x]
            page_order[x] = page_order[y]
            page_order[y] = tmp

            # Restart from the beginning
            i = 0 
            continue

        i += 1

    # Skip already valid page orders
    if not invalid:
        return 0
        
    # Return middle page number
    for page_num, index in page_order.items():
        if index == (len(page_order)-1) / 2:
            return page_num

def main():
    lines = get_lines_from_file("input.txt")

    rules, page_orders_list = get_data(lines)

    sum = 0
    for page_order in page_orders_list:
        sum += process_page_order(page_order, rules)
            
    print(f"sum: {sum}")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"elapsed time: {(time.time() - start):.4f} seconds")