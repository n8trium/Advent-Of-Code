total=0
num_list=[]
map=[]
digit_list=[]
line_count=0
with open("example01.txt") as fp:
    for line in fp:
        map.append(line.strip())

def coords(map):
    symbols=[]
    digits=[]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x].isdigit():
                digits.append((x, y))
            elif map[y][x]==".":
                pass
            else:
                symbols.append((x, y))
    return(digits, symbols)

def touch_nums(x, line):
    if not line[x].isdigit():
        return None
    start=x
    while start > 0 and line[start - 1].isdigit():
        start-=1
    end = x
    while end < len(line) - 1 and line[end+1].isdigit():
        end+=1
    return int(line[start:end + 1])

numbers, ids = coords(map)
for num_coord in numbers:
    for id_coord in ids:
        if id_coord[1]-1==num_coord[1]:
            bin_counter=0
            if id_coord[0]-1==num_coord[0]:
                bin_counter=1
                digit_list.append(num_coord)
            if id_coord[0]==num_coord[0]:
                if bin_counter==1:
                    bin_counter=2
                    pass
                else:
                    bin_counter=2
                    digit_list.append(num_coord)
            if id_coord[0]+1==num_coord[0]:
                if bin_counter!=2:
                    digit_list.append(num_coord)
        if id_coord[1]==num_coord[1]:
            bin_counter=0
            if id_coord[0]-1==num_coord[0]:
                bin_counter=1
                digit_list.append(num_coord)
            if id_coord[0]==num_coord[0]:
                if bin_counter==1:
                    bin_counter=2
                    pass
                else:
                    bin_counter=2
                    digit_list.append(num_coord)
            if id_coord[0]+1==num_coord[0]:
                if bin_counter!=2:
                    digit_list.append(num_coord)
        if id_coord[1]+1==num_coord[1]:
            bin_counter=0
            if id_coord[0]-1==num_coord[0]:
                bin_counter=1
                digit_list.append(num_coord)
            if id_coord[0]==num_coord[0]:
                if bin_counter==1:
                    bin_counter=2
                    pass
                else:
                    bin_counter=2
                    digit_list.append(num_coord)
            if id_coord[0]+1==num_coord[0]:
                if bin_counter!=2:
                    digit_list.append(num_coord)

for i in range(len(digit_list)):
    x=digit_list[i][0]
    y=digit_list[i][1]
    num=touch_nums(x, map[y])
    num_list.append(num)
    print(num_list)
    total+=num

#print(f"Digits: {digit_list}")
#print(f"Num: {num_list}")
#print(f"Symbols: {ids}")

print(f"Total: {total}")
