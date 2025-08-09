import math
with open("input.txt") as fp:
    input=fp.readlines()

instructions=input[0].strip()
print(instructions)
path={}
nodes=[]
for line in input[2:]:
    key, code = line.strip().split(" = ")
    left=code[1:4]
    right=code[6:9]
    path[key]=(left, right)
    if key[2]=="A":
        nodes.append(key)

print(nodes)
path_lengths=[]

for z in nodes:
    steps=0
    x=-1
    while z[2] != "Z":
        print(f"{z}")
        x+=1
        if x == len(instructions):
            x=0
        if instructions[x] == "L":
            z=path[z][0]
            steps+=1
        elif instructions[x] == "R":
            z=path[z][1]
            steps+=1
    path_lengths.append(steps)



print(path_lengths)
first=path_lengths[0]
for i in range(len(path_lengths)):
    second=path_lengths[i]
    first=math.lcm(first, second)
print(f"Ssteps: {first}")