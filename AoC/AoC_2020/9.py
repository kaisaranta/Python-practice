from itertools import combinations

with open ("input_2020_09.txt") as file:
    data = [int(line) for line in file.readlines()]

# Part One
for index in range(25, len(data)):
    pairs = combinations(data[index-25:index], 2)
    if not [True for pair in pairs if pair[0] + pair[1] == data[index]]:
        result_1 = data[index]
        break

print(f"Part One: The first number is {result_1}.")

# Part Two
start_index = 0
total = 0
while total != result_1: 
    total = data[start_index]    
    next_index = start_index + 1
    while total < result_1:
        total += data[next_index] 
        if total == result_1:
            result_2 = min(data[start_index:next_index+1])+max(data[start_index:next_index+1])
            break
        next_index += 1
    start_index += 1

print(f"Part Two: The encryption weakness is {result_2}.")

