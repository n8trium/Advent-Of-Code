with open("input.txt", "r") as fp:
    lines=fp.read()

input=lines.split("\n\n")
seed_raw=input[0].split(" ")[1:]
seeds=seed_raw[::2]
seed_range=seed_raw[1::2]
#print(input)
print(seeds)
print(seed_range)

def map_fix(map):
    m_in=[]
    out=[]
    range=[]
    for i in map.split("\n")[1:]:
        tmp=i.split(" ")
        if len(tmp)==3:
            m_in.append(int(tmp[1]))
            out.append(int(tmp[0]))
            range.append(int(tmp[2]))
    return(m_in, out, range, map.split("\n")[0])

def converter(map_in, map_out, map_range, value):
    for i in range(len(map_in)):
        if map_in[i] <= value < map_in[i]+map_range[i]:
            return(value-map_in[i]+map_out[i])
        else:
            if i==len(map_in)-1:
                return(value)
locations=[]
maps=input[1:]
for j in range(len(seeds)):
    k=0
    while k < int(seed_range[j]):
        new=int(k)+int(seeds[j])
        for i in range(len(maps)):
            mi, mo, mr, name=map_fix(maps[i])
            new=converter(mi, mo, mr, new)
        locations.append(new)
        k+=1
print(min(locations))