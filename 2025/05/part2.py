fresh_low=[]
fresh_high=[]
ingredients=[]
ranges=True
with open("input.txt") as fp:
    for line in fp:
        if ranges:
            if line == "\n":
                ranges=False
            else:
                fresh_low.append(int(line.strip().split("-")[0]))
                fresh_high.append(int(line.strip().split("-")[-1]))
        else:
            ingredients.append(int(line.strip()))
fresh=0
for i in ingredients:
    for j in range(len(fresh_low)):
        if fresh_low[j] <= i <= fresh_high[j]:
            fresh+=1
            break
print(fresh)