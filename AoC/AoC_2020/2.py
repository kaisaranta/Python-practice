with open ("input_2020_02.txt") as file:
    data = [line.split() for line in file.readlines()]

counter_1 = 0
counter_2 = 0
for line in data:
    start, end = map(int, line[0].split("-"))
    letter = line[1][0]
    if line[2].count(letter) in range(start, end+1):
        counter_1 += 1
    if line[2][start-1] == letter and line[2][end-1] == letter:
        continue
    if line[2][start-1] == letter or line[2][end-1] == letter:
        counter_2 += 1

print(f"Part One: {counter_1} passwords are valid.")
print(f"Part Two: {counter_2} passwords are valid.")

