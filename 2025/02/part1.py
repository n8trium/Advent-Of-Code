with open("input.txt") as fp:
    ranges=fp.readline().strip().split(",")
invalid=0
bottom=[]
top=[]
for i in range(len(ranges)):
    bottom.append(int(ranges[i].split("-")[0]))
    top.append(int(ranges[i].split("-")[1]))

low=sorted(bottom)
high=sorted(top)

print(low, high)

dig_l=len(str(low[0]))//2
dig_h=len(str(high[-1]))//2

if dig_l==0:
    dig_l=1

print(int(str(low[0])[:dig_l]), int(str(high[-1])[:dig_h]))

for x in range(int(str(low[0])[:dig_l]), int(str(high[-1])[:dig_h])):
    y=int(str(x)+str(x))
    for z in range(len(low)):
        if y>=low[z] and y <=high[z]:
            invalid+=y
print(invalid)