with open("input_2019_1.txt") as file:
    data = [int(mass) for mass in file.readlines()]

#Part One
total_1 = sum(mass//3 - 2 for mass in data)

print(f"Part One: The sum of the fuel requirements is {total_1}.")

#Part Two
total_2 = 0

for mass in data:
    mass = mass//3 - 2
    while mass > 0:
        total_2 += mass
        mass = mass//3 - 2

print(f"Part Two: The sum of the fuel requirements is {total_2}.")

