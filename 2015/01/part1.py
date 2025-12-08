floor=0

with open("input.txt") as fp:
    line=fp.readline()

for char in line:
    if char == "(":
        floor += 1
    if char == ')':
        floor -=1

print(floor)