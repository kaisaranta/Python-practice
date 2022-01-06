with open("input_2018_5.txt") as file:
    polymer = file.read()

def collapse(polymer):
    index = 0
    while index < len(polymer)-1:
        if polymer[index] == polymer[index+1].swapcase():
            polymer = polymer[:index] + polymer[index+2:]
            index = index - 1 if index != 0 else 0
        else:
            index += 1
    return len(polymer)

# Part One
print(f"Part One: {collapse(polymer)} units remain.")

# Part Two
lengths = []

for letter in "abcdefghijklmnopqrstuvwxyz":
    new_polymer = polymer.replace(letter, "").replace(letter.swapcase(), "")
    lengths.append(collapse(new_polymer))

print(f"Part Two: The length of the shortest polymer is {min(lengths)}.")