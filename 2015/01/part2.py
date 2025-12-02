floor=0

with open("input.txt") as fp:
    line=fp.readline()

for char in range(len(line)):
    #print(char, floor)
    if line[char] == "(":
        floor += 1
    elif line[char] == ')':
        floor -= 1
    
    if floor == -1:
        print(char+1)
        break