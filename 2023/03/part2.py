total=0
num_list=[]
map=[]
digit_list=[]
line_count=0
with open("input.txt") as fp:
    for line in fp:
        map.append(line.strip())

def coords(map):
    gears=[]
    digits=[]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x].isdigit():
                digits.append((x, y))
            elif map[y][x]==".":
                pass
            else:
                gears.append((x, y))
    return(digits, gears)

nums, gears = coords(map)

def make_numlist(nums, map):
    num_list=[]
    current_number=str(map[nums[0][1]][nums[0][0]])
    indexes=[]
    for index in range(len(nums)):
        #print(current_number)
        if index+1<len(nums):
            #print(indexes)
            if nums[index+1][1]==nums[index][1]:
                #print(map[nums[index][1]])
                if nums[index+1][0]==nums[index][0]+1:
                    indexes.append((nums[index][0], nums[index][1]))
                    current_number=current_number+str(map[nums[index+1][1]][nums[index+1][0]])
                else:
                    indexes.append((nums[index][0], nums[index][1]))
                    num_list.append([current_number, indexes, False])
                    indexes=[]
                    current_number=str(map[nums[index+1][1]][nums[index+1][0]])
            else:
                indexes.append((nums[index][0], nums[index][1]))
                num_list.append([current_number, indexes, False])
                indexes=[]
                current_number=str(map[nums[index+1][1]][nums[index+1][0]])
        else:
            indexes.append((nums[index][0], nums[index][1]))
            num_list.append([current_number, indexes, False])
            indexes=[]
    return(num_list)

pairs=make_numlist(nums, map)
print(pairs)
for vars in range(len(gears)): # loop through each gear
    #print(f"gear: {map[gears[vars][1]][gears[vars][0]]} @ {gears[vars]}")
    x_n=gears[vars][0]
    y_n=gears[vars][1]
    gear_counter=0
    gear_ratio=1
    for x in range(x_n-1, x_n+2): #loop through x's
        for y in range(y_n-1, y_n+2): # loop throgh y's
            for i in range(len(pairs)):
                for j in range(len(pairs[i][1])):
                    #print(f"x_1: {x}, y_1: {y}, x_2, y_2: {pairs[i][1]}")
                    if pairs[i][1][j] == (x, y):
                        if pairs[i][2]==False:
                            gear_counter+=1
                            gear_ratio*=int(pairs[i][0])
                            pairs[i][2]=True
                            print(f"New: {pairs[i][0]}")
    if gear_counter==2:
        total+=gear_ratio

print(f"Total: {total}")
