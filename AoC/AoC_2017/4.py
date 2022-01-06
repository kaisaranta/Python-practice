with open("input_2017_4.txt") as file:
    data = [line.split() for line in file.readlines()]

# Part One
res_1 = sum(1 for line in data if len(line) == len(set(line)))

print(f"Part One: {res_1} passphrases are valid.")

#¤ Part Two
res_2 = sum(1 for line in data if len(line) == len(set(["".join(sorted(word)) for word in line])))          

print(f"Part Two: {res_2} passphrases are valid.")