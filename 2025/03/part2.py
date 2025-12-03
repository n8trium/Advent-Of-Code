total=0

def biggest_index(i0, i1, bat):
    if i1==0:
        return(max(range(len(battery[i0:])), key=battery[i0:].__getitem__))
    else:
        return(max(range(len(battery[i0:i1])), key=battery[i0:i1].__getitem__))

with open("input.txt") as fp:
    for line in fp:
        battery=[]
        for x in line.strip():
            battery.append(int(x))
        indexes=[biggest_index(0, -11, battery)]
        for end_index in range(-10, 1):
            indexes.append(biggest_index(indexes[-1]+1, end_index, battery)+indexes[-1]+1)
        joltage=""
        for i in range(len(indexes)):
            joltage+=str(battery[indexes[i]])
        total+=int(joltage)
print(total)