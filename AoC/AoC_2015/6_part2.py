def switch(light, setting):
    if setting == "on":
        return light + 1
    elif setting == "off":
        if light == 0:
            return 0
        else:
            return light - 1
    else:
        return light + 2

with open("input_2015_6.txt") as file:
    data = [line.split() for line in file.readlines()]

grid = {}
for x in range(1000):
    for y in range(1000):
        grid[x, y] = 0

for line in data:
    start_x, start_y = map(int, line[-3].split(","))
    end_x, end_y = map(int, line[-1].split(","))

    if "on" in line:
        setting = "on"
    elif "off" in line:
        setting = "off"
    else:
        setting = "toggle"

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            grid[(i, j)] = switch(grid[(i, j)], setting)

print(f"Part Two: The total brightness is {sum(grid.values())}.")