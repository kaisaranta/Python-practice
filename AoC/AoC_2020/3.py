with open ("input_2020_03.txt") as file:
    data = [line.strip() for line in file.readlines()]

def count_trees(map, step_right, step_down):
    counter = 0
    pos = 0
    line_counter = 0 # For Part Two
    for line in map[1:]:
        line_counter += 1
        if line_counter % step_down != 0:
            continue
        pos += step_right
        while pos >= len(line):
            line += line
        if line[pos] == "#":
            counter += 1
    return counter

#Part One
print(f"Part One: {count_trees(data, 3, 1)} trees")

#Part Two
res = count_trees(data, 1, 1)*count_trees(data, 3, 1)*count_trees(data, 5, 1)*count_trees(data, 7, 1)*count_trees(data, 1, 2)
print(f"Part Two: {res} trees")