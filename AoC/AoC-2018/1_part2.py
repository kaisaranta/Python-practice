with open("input_2018_1.txt") as file:
    data = [int(item) for item in file.readlines()]

frequency = 0
frequencies = set()
found = False

while found == False:
    for number in data:
        frequency += number
        if frequency in frequencies:
            print(f"Part Two: The first frequency reached twice is {frequency}.")
            found = True
            break
        frequencies.add(frequency)