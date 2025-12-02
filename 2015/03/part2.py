with open("input.txt") as fp:
    line = fp.readline()

def write_coords(x, y, char):
    match char:
        case "^":
            y+=1
        case "v":
            y-=1
        case ">":
            x+=1
        case "<":
            x-=1
    return x, y
    
xs=0
ys=0
xr=0
yr=0
s_coords=[(0,0)]
r_coords=[(0,0)]

for i in line[::2]:
    xs, ys = write_coords(xs, ys, i)
    s_coords.append((xs, ys))
for j in line[1::2]:
    xr, yr = write_coords(xr, yr, j)
    r_coords.append((xr, yr))
coords=s_coords
for k in r_coords:
    coords.append(k)
print(len(list(set(coords))))