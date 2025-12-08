import math
junction_boxes={}
count=0
with open('example01.txt') as fp:
    for line in fp:
        count+=1
        junction_boxes[count]=tuple(map(int, line.rstrip().split(',')))

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

circuits={}
circuit_count=0

# This won't work. Fix the elifs and the if (don't check correct value and circuit count of elif is wrong)

for i in list(arranged.keys())[:10]:
    box1, box2 = int(i.split('-')[0].strip()), int(i.split('-')[1].strip())
    if box1 not in circuits and box2 not in circuits:
        circuit_count+=1
        circuits[circuit_count]=[box1, box2]
    elif box1 not in circuits:
        circuits[circuit_count].append(box1)
    elif box2 not in circuits:
        circuits[circuit_count].append(box2)

print(circuits)