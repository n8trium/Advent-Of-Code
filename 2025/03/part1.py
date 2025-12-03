total=0
with open("input.txt") as fp:
    for line in fp:
        battery=[]
        for x in line.strip():
            battery.append(int(x))
        first_index=max(range(len(battery[:-1])), key=battery[:-1].__getitem__)
        second=max(battery[first_index+1:])
        total+=int(str(battery[first_index])+str(second))
        print(total)
print(total)