num = "3113322113"
i = 0

while i < 50:
    prev = num[0]
    counter = 1
    res = ""
    for digit in num[1:]:
        if digit == prev:
            counter += 1
        else:
            res += str(counter) + prev
            counter = 1
        prev = digit
    num = res + str(counter) + digit
    i += 1
    if i == 40:
        print(f"Part One: The length of the result is {len(num)}.")

print(f"Part Two: The length of the result is {len(num)}.")