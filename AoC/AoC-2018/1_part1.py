with open("input_2018_1.txt") as file:
    print(f"Part One: Resulting frequency is {sum([int(item) for item in file.readlines()])}.")