with open("input_2017_2.txt") as file:
    data = [tuple(map(int, line.split())) for line in file.readlines()]

# Part One
checksum = sum((max(line) - min(line)) for line in data)
print(f"Part One: The checksum is {checksum}.")

# Part Two
total = 0

for line in data:
    for divisible in line:
        for divisor in line:
            if divisible % divisor == 0 and divisible != divisor:
                total += divisible/divisor

# Using list comprehension:
# total = (sum(divisible/divisor for line in data for divisible in line for divisor in line if divisible % divisor == 0 and divisible != divisor))

print(f"Part Two: The sum is {int(total)}.")