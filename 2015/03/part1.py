with open("input.txt") as fp:
    line = fp.readline()

x=0
y=0
coords=[(0,0)]

for char in line:
    match char:
        case "^":
            y+=1
        case "v":
            y-=1
        case ">":
            x+=1
        case "<":
            x-=1
    coords.append((x, y))

print(len(list(set(coords))))