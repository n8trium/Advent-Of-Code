coords=set()
with open('example01.txt') as fp:
    for line in fp:
        coords.add((int(line.strip().split(',')[0]), int(line.strip().split(',')[1])))

area=0
for i in coords:
    for j in coords:
        if j > i:
            curr = int(abs(i[1]-j[1])+1) * int(abs(j[0]-i[0])+1)
            if curr > area:
                area=curr
print(area)