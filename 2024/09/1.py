#debug this...

total=0
data = ''
disk_map=''
with open('example2.txt') as fp:
    for line in fp:
        data+=line
print(data)

for i in range(len(data)):
    if i%2==0:
        x=0
        while x < int(data[i]):
            disk_map+=str(i//2)
            x+=1
    else:
        x=0
        while x < int(data[i]):
            disk_map+='.'
            x+=1

j=len(disk_map)-1
for i in range(len(disk_map)):
    if disk_map[i]=='.': # find next free spot
        while j > i:
            print(i, j)
            if disk_map[j]!='.': # find last spot with data
                print('swapping!')
                disk_map = disk_map[:i] + disk_map[j] + disk_map[i+1:]
                disk_map = disk_map[:j] + '.' + disk_map[j+1:]
                break
            else:
                j-=1
print(disk_map)
for i in range(len(disk_map)):
    if disk_map[i].isdigit():
        total+=i*int(disk_map[i])
print(f'Total: {total}')