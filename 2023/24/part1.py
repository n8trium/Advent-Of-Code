with open ("input.txt") as fp:
    input=fp.readlines()
px=[]
py=[]
pz=[]
vx=[]
vy=[]
vz=[]
for line in input:
    pos, vel=line.strip().split("@")
    px.append(int(pos.strip().split(",")[0]))
    py.append(int(pos.strip().split(",")[1]))
    pz.append(int(pos.strip().split(",")[2]))
    vx.append(int(vel.strip().split(",")[0]))
    vy.append(int(vel.strip().split(",")[1]))
    vz.append(int(vel.strip().split(",")[2]))

print(px, py, pz, vx, vy, vz)

def collision(px1, py1, m1, px2, py2, m2):
    b1=py1-m1*px1
    b2=py2-m2*px2
    if m1==m2:
        print("parallel")
        return False
    x_int=(b1-b2)/(m2-m1)
    y_int=x_int*m1+b1
    if 200000000000000 < x_int < 400000000000000:
        if 200000000000000 < y_int < 400000000000000:
            print(f"{i}, {j}, {x_int}, {y_int}")
            if (px1-x_int)/vx[i] > 0:
                return False
            elif (px2-x_int)/vx[j] > 0:
                return False
            else:
                #print(f"Coords: {x_int}, {y_int}")
                return True
    else:
        return False

counter=0
for i in range(len(px)):
    for j in range(len(px)):
        if j > i:
            #print(j, i)
            if collision(px[i], py[i], vy[i]/vx[i], px[j], py[j], vy[j]/vx[j]):
                #print(j, i)
                counter+=1
print(counter)