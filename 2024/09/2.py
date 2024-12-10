# Advent of Code
# Day 9
# Part 1
# n8trium

total=0
data = []
disk_map = []
with open('example.txt') as fp:
    for line in fp:
        data+=line
print(data)

for i in range(len(data)):
    if i%2==0:
        x=0
        while x < int(data[i]):
            disk_map.append(str(i//2))
            x+=1
    else:
        x=0
        while x < int(data[i]):
            disk_map.append('.')
            x+=1

j=len(disk_map)-1
while j>=0:
    if disk_map[j]!='.':
        k=j-1
        if disk_map[k]==disk_map[j]:
            k-=1
        space=j-k
        k+=1
        print(space)
        i=0
        while i<j:
            if disk_map[i]=='.':
                m=1
                while m<space:
                    pass
            i+=1
        j=k-1
    else:
        j-=1

for i in range(len(disk_map)):
    print(disk_map[i], end='')
    if disk_map[i].isdigit():
        total+=i*int(disk_map[i])
print(f'\n\nTotal: {total}')