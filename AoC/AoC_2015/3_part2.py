with open("input_2015_3.txt") as file:
    data = file.read()

def number_of_houses(data: str):
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
    
    return houses

print(f"Part 1: Santa visits {len(number_of_houses(data))} houses.")

santa_route = [data[index] for index in range(len(data)) if index % 2 == 0]
robosanta_route = [data[index] for index in range(len(data)) if index % 2 != 0]

print(f"Part 2: Santa and Robo-Santa visit {len(set(number_of_houses(santa_route) + number_of_houses(robosanta_route)))} houses.")