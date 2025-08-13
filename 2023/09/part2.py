total=0

with open("input.txt") as fp:
    input=fp.readlines()

def recurser(numline, number):
    line2=[]
    print(numline)
    for i in range(len(numline)-1):
        b=numline[i+1]-numline[i]
        line2.append(b)
    k=0
    number-=line2[0]
    print(number)
    for j in line2:
        if j==0:
            k+=1
    if k==len(line2):
        print(f"k: {k}")
        print(number)
        return number
    else:
        print(f"Recursion Here!, {k}")
        return recurser(line2, number)

for line in input:
    array=line.strip().split(" ")
    for i in range(len(array)):
        array[i]=int(array[i])
    perline = recurser(array, array[0])
    print(f"perline: {perline}")
    total+=perline

print(f"Total: {total}")