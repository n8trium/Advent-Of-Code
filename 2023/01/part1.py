def checker(char):
    if char=="0":
        return(int(char))
    if char=="1":
        return(int(char))
    if char=="2":
        return(int(char))
    if char=="3":
        return(int(char))
    if char=="4":
        return(int(char))
    if char=="5":
        return(int(char))
    if char=="6":
        return(int(char))
    if char=="7":
        return(int(char))
    if char=="8":
        return(int(char))
    if char=="9":
        return(int(char))
    if char=="0":
        return(int(char))

sum=0
with open("input.txt") as fp:
    for line in fp:
        print(line)
        print(f"length: {len(line)-1}")
        for char in range(len(line)):
            if checker(line[char]) != None:
                a=checker(line[char])
                break
        for char in range(len(line)-1, -1, -1):
            #print(char)
            if checker(line[char]) != None:
                b=checker(line[char])
                break
        c=int(str(a)+str(b))
        print(f"a: {a} b: {b} c: {c}")
        sum+=c
print(f"Sum: {sum}")

