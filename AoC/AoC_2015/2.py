with open("input_2015_2.txt") as file:
    data = [line.split("x") for line in file.readlines()]

total = 0
ribbon = 0

for line in data:
    l, w, h = map(int, line)
    short_1 = sorted([l, w, h])[0]
    short_2 = sorted([l, w, h])[1]
    total += 2*l*w + 2*w*h + 2*h*l + short_1 * short_2
    ribbon += 2 * short_1 + 2 * short_2 + l*w*h

print(f"Part 1: The elves need {total} square feet of paper")
print(f"Part 1: The elves need {ribbon} feet of ribbon")




