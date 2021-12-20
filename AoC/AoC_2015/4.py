import hashlib

number = 0
found1 = False
found2 = False

while not found2:
    result = hashlib.md5(("bgvyzdsv"+str(number)).encode())
    val_hex = result.hexdigest()
    if val_hex[:5] == "00000" and not found1:
        print(f"Part One: The lowest positive number is {number}.")
        found1 = True
    if val_hex[:6] == "000000":
        print(f"Part Two: The lowest positive number is {number}.")
        found2 = True
    number += 1
    