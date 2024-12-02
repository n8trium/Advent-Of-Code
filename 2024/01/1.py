# Advent of code
# Day 1
# Part 1

total = 0 # our total subtracted from each list
b=[] # first list
c=[] # second list

with open("input.txt") as lines:
    for line in lines: # iterate through each file
        a = line.split("   ") # splits into two lists: b & c
        b.append(int(a[0])) # makes list b
        c.append(int(a[1])) # makes list c
b.sort() # sort in ascending manner
c.sort() # sort in ascending manner
for i in range(len(b)): # iterate over b
    total+=(abs(b[i]-c[i])) # add each subtracted absolute value to our total
print(total) # print the total