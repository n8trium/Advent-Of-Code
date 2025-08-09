with open("input.txt") as fp:
    input=fp.readlines()

time=list(filter(None, input[0].strip("\n").split(" ")))[1:]
distance=list(filter(None, input[1].strip("\n").split(" ")))[1:]
print(time)
print(distance)
ways=1
for x in range(len(distance)):
    way=0
    mm=int(distance[x])
    ms=int(time[x])
    for y in range(0, ms):
        t=y*(ms-y)
        if t > mm:
            way+=1
    ways*=way

print(ways)