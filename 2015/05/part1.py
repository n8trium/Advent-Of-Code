total=0
def line_test(string):
    vowels=0
    doubles=0
    for i in range(len(string)):
        if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
            vowels+=1
        if i != len(string)-1:
            j=i+1
            if string[j]==string[i]:
                doubles+=1
            for k in ["ab", "cd", "pq", "xy"]:
                if str(string[i]+string[j])==k:
                    return(0)
    if vowels < 3:
        return(0)
    elif doubles == 0:
        return(0)
    else:
        return(1)
        

with open("input.txt") as fp:
    for line in fp:
        total+=line_test(line.strip())

print(total)