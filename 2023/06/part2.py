with open("input.txt") as fp:
    input=fp.readlines()
time=""
distance=""
times=list(filter(None, input[0].strip("\n").split(" ")))[1:]
distances=list(filter(None, input[1].strip("\n").split(" ")))[1:]
for i in times:
    time=time+i
for i in distances:
    distance=distance+i
time=int(time)
distance=int(distance)
print(time)
print(distance)
ways=1

for ms in range(0, time):
    x=ms*(time-ms)
    if x > distance:
        break

for max in range(time, 0, -1):
    x=max*(time-max)
    if x > distance:
        break
print(max-ms+1)
