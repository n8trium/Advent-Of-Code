# Advent of code
# Day 1
# Part 2

total = 0 # our total subtracted from each list
b=[] # first list
c=[] # second list

with open("input.txt") as lines:
    for line in lines: # iterate through each file
        a = line.split("   ") # splits into two lists: b & c
        b.append(int(a[0])) # makes list b
        c.append(int(a[1])) # makes list c

for i in range(len(b)): # iterate over b
    for j in range(len(c)): # iterate over c
        if b[i]==c[j]: # compare numbers
            total+=(c[j]) # add each value to the similarity total
print(total) # print the total