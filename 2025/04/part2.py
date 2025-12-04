startingmap = [line.rstrip() for line in open('input.txt')]
total=0
def checkpaper(papermap):
    current_count=0
    for y in range(len(papermap)):
        for x in range(len(papermap[y])):
            rollcount=0
            if papermap[y][x] == "@":
                rollcount=0
                for y1 in range(y-1, y+2):
                    if 0 <= y1 < len(papermap):
                        for x1 in range(x-1, x+2):
                            if 0 <= x1 < len(papermap[y1]):
                                if papermap[y1][x1] == "@":
                                    rollcount+=1
                if rollcount < 5:
                    papermap[y]=papermap[y][:x]+"x"+papermap[y][x+1:]
                    current_count+=1
    return current_count, papermap

change=1000000
newmap=startingmap
while change != 0:
    change, newmap = checkpaper(newmap)
    total+=change
print(total)