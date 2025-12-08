total=0
def line_test(string):
    rules=[False, False]
    for i in range(len(string)-2):
        k=i+2
        if string[k]==string[i]:
            rules[0]=True
            break
    for i in range(len(string)-3):
        for k in range(i+2, len(string)-1):
            if str(string[i]+string[i+1])==str(string[k]+string[k+1]):
                rules[1]=True
                break
    if rules[0]==True and rules[1]==True:
        return(1)
    else:
        return(0)

with open("input.txt") as fp:
    for line in fp:
        total+=line_test(line.strip())

print(total)