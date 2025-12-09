coords=set()
with open('example01.txt') as fp:
    for line in fp:
        coords.add((int(line.strip().split(',')[0]), int(line.strip().split(',')[1])))

area=0
print(coords)
coords=list(sorted(coords))
print(coords)
print(len(coords))
counter=0
for i in coords:
    for j in coords:
        if j > i:
            curr = int(abs(i[1]-j[1])+1) * int(abs(j[0]-i[0])+1)
            if curr > area:
                for k in coords:
                    counter+=1
                    if k == i or k == j:
                        pass
                    elif min(i[0], j[0]) < k[0] < max(i[0], j[0]) or min(i[1], j[1]) < k[1] < max(i[1], j[1]):
                        pass # do something here???
                area=curr
print(area)