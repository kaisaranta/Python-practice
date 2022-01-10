with open ("input_2020_06.txt") as file:
    data = file.read().split("\n\n")

# Part One
data_1 = [line.replace("\n", "") for line in data]

total_1 = sum(len(set(letter for letter in line)) for line in data_1)

print(f"Part One: The sum of the counts is {total_1}.")

# Part Two
data_2 = [set(line.split("\n")) for line in data]

total_2 = 0
for group in data_2:
    answers = [set(letter for letter in answer) for answer in group]
    common = set(answers[0]).intersection(*answers)
    total_2 += len(common)

print(f"Part Two: The sum of the counts is {total_2}.")
        



