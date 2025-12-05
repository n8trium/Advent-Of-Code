temp=[]
ingredients=set()
ranges=True
with open("input.txt") as fp:
    for line in fp:
        if line == "\n":
            break
        temp.append((int(line.strip().split("-")[0]), int(line.strip().split("-")[-1])))

fresh=sorted(temp)
total=0

right=-1
for id_range in fresh:
    left = max(right+1, id_range[0])
    right = max(right, id_range[1])
    total += max(0, right-left+1)
print(total)