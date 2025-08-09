with open("input.txt") as fp:
    input=fp.readlines()

instructions=input[0].strip()
print(instructions)
path={}
for line in input[2:]:
    key, code = line.strip().split(" = ")
    left=code[1:4]
    right=code[6:9]
    path[key]=(left, right)

print(path["AAA"])

node="AAA"
steps=0
x=-1
while node != "ZZZ":
    print(f"{node}")
    x+=1
    if x == len(instructions):
        x=0
    if instructions[x] == "L":
        node=path[node][0]
        steps+=1
    elif instructions[x] == "R":
        node=path[node][1]
        steps+=1
    else:
        print("What?")
        break
print(f"node: {node}, steps: {steps}")