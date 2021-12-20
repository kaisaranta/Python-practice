with open("input_2015_3.txt") as file:
    data = file.read()

x = 0
y = 0
houses = [(0, 0)]

for merkki in data:
    if merkki == ">":
        x += 1
    elif merkki == "<":
        x -= 1
    elif merkki == "^":
        y += 1
    else:
        y -= 1
    if (x, y) not in houses:
        houses.append((x, y))

print(f"Part 1: Santa visits {len(houses)} houses.")

x = y = a = b = 0

houses = [(0, 0)]
turn = 0

for merkki in data:
    if turn % 2 == 0:
        if merkki == ">":
            x += 1
        elif merkki == "<":
            x -= 1
        elif merkki == "^":
            y += 1
        else:
            y -= 1
        if (x, y) not in houses:
            houses.append((x, y))
    else:
        if merkki == ">":
            a += 1
        elif merkki == "<":
            a -= 1
        elif merkki == "^":
            b += 1
        else:
            b -= 1
        if (a, b) not in houses:
            houses.append((a, b))
    turn += 1

print(f"Part 2: Santa and Robo-Santa visit {len(houses)} houses.")
        

