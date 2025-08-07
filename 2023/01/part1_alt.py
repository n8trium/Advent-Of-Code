total=0
with open("input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        digits = [x for x in line if x.isdigit()]
        total+=int(digits[0] + digits[-1])
print(f"Total: {total}")