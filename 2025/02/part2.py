with open("input.txt") as fp:
    ranges=fp.readline().strip().split(",")
invalid=[]
bottom=[]
top=[]
for i in range(len(ranges)):
    bottom.append(int(ranges[i].split("-")[0]))
    top.append(int(ranges[i].split("-")[1]))

low=sorted(bottom)
high=sorted(top)

dig_l=len(str(low[0]))//2
dig_h=len(str(high[-1]))//2

if dig_l==0:
    dig_l=1

for x in range(int(str(low[0])[:dig_l]), int(str(high[-1])[:dig_h])):
    for n in range(2, (dig_h//(len(str(x))))+10):
        y=int("".join(str(x)*n))
        for z in range(len(low)):
            if y>=low[z] and y <=high[z]:
                invalid.append(y)
print(sum(list(set(invalid))))