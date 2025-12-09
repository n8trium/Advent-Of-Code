coords=[]
with open('input.txt') as fp:
    for line in fp:
        coords.append((int(line.strip().split(',')[0]), int(line.strip().split(',')[1])))
area=0
for i in range(len(coords)):
    for j in range(len(coords)):
        if j > i:
            curr = int(abs(coords[j][1]-coords[i][1])+1) * int(abs(coords[j][0]-coords[i][0])+1)
            if curr > area:
                area=curr
print(area)