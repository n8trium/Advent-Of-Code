tachyon_map = [line.rstrip() for line in open('input.txt')]
beams={tachyon_map[0].find('S') : 1}
splits=0
new_beams={tachyon_map[0].find('S') : 1}

for line in range(1, len(tachyon_map)):
    for beam in beams:
        if tachyon_map[line][beam]=='^':
            incoming=beams[beam]
            if beam+1 in new_beams:
                new_beams[beam+1]+=incoming
            else:
                new_beams[beam+1]=incoming
            if beam-1 in new_beams:
                new_beams[beam-1]+=incoming
            else:
                new_beams[beam-1]=incoming
            del new_beams[beam]
    beams=new_beams.copy()
print(sum(list(new_beams.values())))