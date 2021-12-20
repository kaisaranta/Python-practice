with open("input_2015_1.txt") as file:
    data = file.read()

floor = 0
counter = 0
entered_basement = False

for merkki in data:
    if floor == -1 and entered_basement == False:
        print(f"Part 2: Santa has entered the basement at position {counter}.")
        entered_basement = True
    if merkki == "(":
        floor += 1
    else:
        floor -= 1
    counter += 1

print(f"Part 1: Santa is at floor {floor}.")