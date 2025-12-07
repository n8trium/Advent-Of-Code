tachyon_map = [line.rstrip() for line in open('input.txt')]
beams=set()
beams.add(tachyon_map[0].find('S'))
splits=0

for line in range(1, len(tachyon_map)):
    for x in range(len(tachyon_map[line])):
        if tachyon_map[line][x] == '^':
            if x in beams:
                beams.add(x-1)
                beams.add(x+1)
                beams.discard(x)
                splits+=1
print(splits)

