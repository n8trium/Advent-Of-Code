import math
junction_boxes={}
count=-1
circuits=[]
with open('input.txt') as fp:
    for line in fp:
        count+=1
        junction_boxes[count]=tuple(map(int, line.rstrip().split(',')))
        circuits.append(set())
        circuits[count].add(count)

def find_distance(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    distance = math.sqrt((abs(x2-x1))**2+(abs(y2-y1))**2+(abs(z2-z1))**2)
    return distance

distances={}
for i in junction_boxes:
    for j in junction_boxes:
        if j > i:
            distances[f'{i}-{j}']=find_distance(junction_boxes[i], junction_boxes[j])

arranged = dict(sorted(distances.items(), key=lambda item: item[1]))
circuit_count=0
for connection in list(arranged.keys()):
    box1, box2 = int(connection.split('-')[0].strip()), int(connection.split('-')[1].strip())
    for i in range(len(circuits)):
        if box1 in circuits[i]:
            break
    for j in range(len(circuits)):
        if box2 in circuits[j]:
            break
    if i != j:
        circuits.append(circuits[i]|circuits[j])
        if i > j:
            del circuits[i]
            del circuits[j]
        else:
            del circuits[j]
            del circuits[i]
    if len(circuits)==1:
        print(junction_boxes[box1][0]*junction_boxes[box2][0])
        break
