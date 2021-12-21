with open("input_2017_1.txt") as file:
    data = file.read()

# Part One
res = sum([int(data[index]) for index in range(len(data)) if data[index] == data[index-1]])
print(f"Part One: The solution is {res}.")


# Part Two
total = 0
for index in range(len(data)):
    if data[index] == data[index - len(data)//2]:
        total += int(data[index])

print(f"The solution is {total}.")