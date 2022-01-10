from itertools import combinations # For Part Two

with open ("input_2020_01.txt") as file:
    data = [int(line) for line in file.readlines()]

#Part One
for line in data:
    if 2020-line in data:
        res_1 = line * (2020-line)
        break

print(f"Part One: Multiplying the two entries results in {res_1}.")

#Part Two
for combination in combinations(data, 3):
    if sum(combination) == 2020:
        res_2 = combination[0] * combination[1] * combination[2]
        break

print(f"Part Two: Multiplying the three entries results in {res_2}.")