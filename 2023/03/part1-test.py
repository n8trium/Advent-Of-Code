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

nums, symbols = coords(map)

print(f"Nums: {nums}")
print(f"Sym: {symbols}")

def make_numlist(nums, map):
    num_list=[]
    current_number=str(map[nums[0][1]][nums[0][0]])
    for index in range(len(nums)):
        print(current_number)
        if index+1<len(nums):
            if nums[index+1][1]==nums[index][1]:
                print(map[nums[index][1]])
                if nums[index+1][0]==nums[index][0]+1:
                    current_number=current_number+str(map[nums[index+1][1]][nums[index+1][0]])
                    print(f"AA: {current_number}")
                else:
                    num_list.append(current_number)
                    current_number=str(map[nums[index+1][1]][nums[index+1][0]])
            else:
                num_list.append(current_number)
                current_number=str(map[nums[index+1][1]][nums[index+1][0]])
        else:
            num_list.append(current_number)
    return(num_list)

make_numlist(nums, map)
print(f"Total: {total}")
