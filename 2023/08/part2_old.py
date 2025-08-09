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
steps=0
x=-1
flag=False
while flag==False:
    check=0
    x+=1
    if x == len(instructions):
        x=0
    for z in range(len(nodes)):
        if instructions[x]=="L":
            nodes[z]=path[nodes[z]][0]
        elif instructions[x]=="R":
            nodes[z]=path[nodes[z]][1]
        if nodes[z][2]=="Z":
            check+=1
        if check==len(nodes):
            flag=True
    print(f"Step: {steps}, {nodes}, {check}")
    steps+=1

print(f"node: {nodes}, steps: {steps}")