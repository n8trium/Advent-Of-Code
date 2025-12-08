with open("input.txt") as fp:
    stones=list(map(int, fp.readline().split()))

def blink(rocks):
    new_stones=[]
    for rock in rocks:
        if rock==0:
            new_stones.append(1)
        elif len(str(rock)) % 2 == 0:
            half=int(len(str(rock)) / 2)
            new_stones.append(int(str(rock)[:half]))
            new_stones.append(int(str(rock)[half:]))
        else:
            new_stones.append(rock*2024)
    return(new_stones)

print(stones)
for i in range(0, 75):
    stones=blink(stones)
    print(i, len(stones))