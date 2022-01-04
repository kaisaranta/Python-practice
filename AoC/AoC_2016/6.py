with open("input_2016_6.txt")as file:
    data = [line.strip() for line in file.readlines()]

res_1 = ""
res_2 = ""
    
for i in range(len(data[0])):
    counter = {}
    for line in data:
        counter[line[i]] = counter.get(line[i], 0) + 1
    res_1 += max(counter, key=lambda x: counter.get(x))
    res_2 += min(counter, key=lambda x: counter.get(x))

print(f"Part One: The message sent is {res_1}.")
print(f"Part One: The message sent is {res_2}.")
