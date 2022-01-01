from itertools import permutations

with open("input_2015_9.txt") as file:
    data = [line.split() for line in file.readlines()]

cities = set()

for line in data:
    cities.add(line[0])
    cities.add(line[2])

distances = set()

for route in permutations(cities, len(cities)):
    total_distance = 0
    for index in range(len(route)-1):
        for line in data:
            if route[index] in line and route[index+1] in line:
                distance = int(line[-1])
                total_distance += distance
                break
    distances.add(total_distance)

print(f"Part One: The distance of the shortest route is {min(distances)}.")

print(f"Part Two: The distance of the longest route is {max(distances)}.")

