# Advent of Code
# 2024
# Day 7
# Part 1
# n8trium

total=0
sum_dict={}
with open("input.txt", 'r') as fp:
    for line in fp:
        tmp=[]
        tmp=line.split(':')
        dict_list=tmp[1].split()
        sum_dict[tmp[0]]=dict_list

def adder(old_list):
    add_val=int(old_list[0])+int(old_list[1])
    if len(old_list)>2:
        new_list=[add_val]+old_list[2:]
        return(new_list)
    else:
        return(add_val)

def mul(old_list):
    mul_val=int(old_list[0])*int(old_list[1])
    if len(old_list)>2:
        new_list=[mul_val]+old_list[2:]
        return(new_list)
    else:
        return(mul_val)
    
def variable_maker(var, new_list):
    if var%2==1: # odd
        new_list.append(1)
        var=var//2
        # print(var, new_list)
        variable_maker(var, new_list)
    else:
        if var==0: # even
            if new_list==[]:
                new_list.append(0)
            return(new_list)
        else:
            new_list.append(0)
            if var%2==0 and var//2==0:
                new_list.append(0)
                return(new_list)
            var=var//2
            variable_maker(var, new_list)
    return(new_list)

for each_total in sum_dict:
    k = 0
    l=len(sum_dict[each_total])-1 # operators needed
    print(f"\nChecking: {each_total} | Combos: {2*(l)}")
    while k < 2**l:
        m=sum_dict[each_total]
        binary=variable_maker(k, [])
        while len(binary) < l:
            binary.append(0) # append zeroes
        print(k, binary)
        for n in range(len(binary)):
            #print(f"M: {m}")
            if binary[n]==0:
                m=adder(m) # adds
                print(f"Add: {m}")
            elif binary[n]==1:
                m=mul(m) # multiplies
                print(f"Mul: {m}")
            else:
                print("Error")
        if int(each_total)==int(m):
            total+=m
            print(f"Running total: {total}")
            break
        else:
            print(f"Comparing: {m}!={each_total}")
        k+=1
    
print(f"Total: {total}")