import re

towers={}
antinodes=[]
data = [line.strip() for line in open('example.txt')]
x_range=len(data[0])
y_range=len(data)
print(x_range, y_range)
hash_map=[]
blank=''
for x in range(x_range):
    blank=blank+('.')
for y in range(y_range):
    hash_map.append(blank)
print(hash_map)

def moving(coords_i, coords_f, delta_x, delta_y, x_max, y_max):
    if 
    y_move=(coords_f[1]-coords_i[1])
    x_move=(coords_f[0]-coords_i[0])
    (x,y)=coords_f[1]+y_move
    return((x, y))


for y in range(len(data)):
    print(data[y])
    for x in range(len(data[y])):
        if re.match('\w', data[y][x]) != None:
            match = re.search('\w', data[y][x])
            if match:
                towers.setdefault(match.group(0), []).append((x, y))
print(towers)
for freq in towers:
    print(f'\n{freq}')
    for first in towers[freq]:
        for second in towers[freq]:
            if second != first:
                print(f'1: {first} 2: {second}')
                nodes=moving(first, second, x_range, y_range)
                if len(nodes) > 0:
                    for i in nodes:
                        antinodes.append(i)
            else:
                break
for i in range(len(antinodes)):
    print(antinodes[i][1], antinodes[i][0])
    hash_map[antinodes[i][1]]=hash_map[antinodes[i][1]][:antinodes[i][0]]+'#'+hash_map[antinodes[i][1]][1+antinodes[i][0]:]
print(sorted(antinodes))
total=0
for y_1 in range(len(hash_map)):
    for x_1 in range(len(hash_map)):
        if hash_map[y_1][x_1]=='#':
            total+=1
    print(hash_map[y_1])
print(total)
