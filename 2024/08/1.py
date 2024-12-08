import re

towers={}
antinodes=[]
data = [line.strip() for line in open('input.txt')]
x_range=len(data[0])
y_range=len(data)
print(x_range, y_range)
hash_map=[]
blank=''
for x in range(x_range):
    blank=blank+('.')
for y in range(y_range):
    hash_map.append(blank)
# print(hash_map)

for y in range(len(data)):
    print(data[y])
    for x in range(len(data[y])):
        if re.match('\w', data[y][x]) != None:
            match = re.search('\w', data[y][x])
            if match:
                towers.setdefault(match.group(0), []).append((x, y))
print(towers)
for freq in towers:
    # print(f'\n{freq}')
    for first in towers[freq]:
        for second in towers[freq]:
            if second != first:
                # print(f'1: {first} 2: {second}')
                positive=(2*second[0]-first[0], 2*second[1]-first[1])
                if 0<=positive[0]<x_range and 0<=positive[1]<y_range:
                    antinodes.append(positive)
                negative=(2*first[0]-second[0], 2*first[1]-second[1])
                if 0<=negative[0]<x_range and 0<=negative[1]<y_range:
                    antinodes.append(negative)
                # print(positive, negative)
            else:
                break
for i in range(len(antinodes)):
    #print(antinodes[i][1], antinodes[i][0])
    hash_map[antinodes[i][1]]=hash_map[antinodes[i][1]][:antinodes[i][0]]+'#'+hash_map[antinodes[i][1]][1+antinodes[i][0]:]
# print(sorted(antinodes))
total=0
for y_1 in range(len(hash_map)):
    for x_1 in range(len(hash_map)):
        if hash_map[y_1][x_1]=='#':
            total+=1
    print(hash_map[y_1])
print(total)
