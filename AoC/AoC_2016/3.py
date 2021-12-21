# Part One
with open("input_2016_3.txt") as file:
    data = [sorted(tuple(map(int, line.split()))) for line in file.readlines()]

counter = 0
for s1, s2, s3 in data:
    if s1 + s2 > s3:
        counter += 1

print(f"Part One: There are {counter} possible triangles.")


# Part Two
with open("input_2016_3.txt") as file:
    data = [int(item) for item in file.read().split()]

counter = 0
for index in range(0, (len(data)-8), 9):
    t1 = (data[index], data[index+3], data[index+6])
    t2 = (data[index+1], data[index+4], data[index+7])
    t3 = (data[index+2], data[index+5], data[index+8])
    for triangle in (t1, t2, t3):
        triangle = sorted(triangle)
        if triangle[0] + triangle[1] > triangle[2]:
                counter += 1

print(f"Part Two: There are {counter} possible triangles.")

