# functions for Part One 

def check_vowels(string):
    counter = 0
    for char in string:
        if char in "aeiou":
            counter += 1
        if counter == 3:
            return True       
    return False

def check_doubles(string):
    for index in range(1, len(string)):
        if string[index] == string[index-1]:
            return True
    return False

def check_forbidden(string):
    for index in range(len(string)-2):
        if string[index:index+2] in ["ab", "cd", "pq", "xy"]:
            return False
    return True

# functions for Part Two

def check_pair(string):
    for index in range(len(string)-2):
        if string[index:index+2] in string[index+2:]:
            return True
    return False

def check_repeat(string):
    for index in range(len(string)-2):
        if string[index] == string[index+2]:
            return True
    return False

with open("input_2015_5.txt") as file:
    data = file.readlines()

counter1 = 0
counter2 = 0
for line in data:
    if check_vowels(line) and check_doubles(line) and check_forbidden(line):
        counter1 += 1
    if check_pair(line) and check_repeat(line):
        counter2 += 1

print(f"Part One: There are {counter1} nice strings.")
print(f"Part Two: There are {counter2} nice strings.")
        

