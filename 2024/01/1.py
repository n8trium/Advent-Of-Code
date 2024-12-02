# Advent of code
# Day 1
# Part 1

total = 0

with open(input.txt) as lines:
    for line in lines:
        a = line.split(" ")
        b = a[0]
        c = a[1]
        total +=abs(b-c)

print(total)