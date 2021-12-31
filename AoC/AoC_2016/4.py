from collections import Counter

with open("input_2016_4.txt") as file:
    data = [line.strip() for line in file.readlines()]

# Part One
total = 0
real_rooms = [] # For Part Two

for line in data:
    index = line.rfind("-")
    new_line = sorted(line[:index].replace("-", ""))
    letters = Counter(new_line)
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    
    checksum = ""   
    for i in range(5):
        checksum += sorted_letters[i][0]

    if checksum == line[-6:-1]:
        total += int(line[index+1:index+4])
        real_rooms.append(line)

print(f"Part One: The sum of the sector IDs is {total}.")

# Part Two
for line in real_rooms:
    short_line = line[:line.rfind("-")]
    id = int(line[-10:-7])
    times = id % 26
    room_name = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in short_line:
        if letter == "-":
            new_letter = " "
        else:
            index = alphabet.index(letter)
            try:
                new_letter = alphabet[index + times]
            except:
                new_letter = alphabet[times - (26 - index)]
        room_name += new_letter
    if room_name == "northpole object storage":
        print(f"Part Two: The sector ID of the room where North Pole objects are stored is {id}.")
        break
    

