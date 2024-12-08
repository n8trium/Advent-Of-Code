# Advent of Code
# 2024
# Day 7
# Part 2
# n8trium

numbers=[]
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

def concat(old_list):
    concat_val=str(old_list[0])+str(old_list[1])
    if len(old_list)>2:
        new_list=[concat_val]+old_list[2:]
        return(new_list)
    else:
        return(int(concat_val))

def variable_maker(var, new_list):
    if var%3==2: # not divisible by 3
        new_list.append(2)
        var=var//3
        # print(var, new_list)
        variable_maker(var, new_list)
    elif var%3==1: # not divisible by 3
        new_list.append(1)
        var=var//3
        # print(var, new_list)
        variable_maker(var, new_list)
    else: # divisible by 3
        if var==0: # even
            if new_list==[]:
                new_list.append(0)
            return(new_list)
        else:
            new_list.append(0)
            if var%3==0 and var//3==0:
                new_list.append(0)
                return(new_list)
            var=var//3
            variable_maker(var, new_list)
    return(new_list)

for each_total in sum_dict:
    k = 0
    l=len(sum_dict[each_total])-1 # operators needed
    print(f"\nChecking: {each_total} | Combos: {3**(l)}")
    while k < 3**l:
        m=sum_dict[each_total]
        binary=variable_maker(k, [])
        while len(binary) < l:
            binary.append(0) # append zeroes
        print(k, binary)
        for n in range(len(binary)):
            if int(m[0]) > int(each_total):
                break
            #print(f"M: {m}")
            if binary[n]==0:
                m=mul(m) # multiplies
                print(f"Add: {m}")
            elif binary[n]==1:
                m=concat(m) # concats
                print(f"Mul: {m}")
            else:
                m=adder(m) # adds
                print(f"Concat: {m}")
        if type(m)!=list:
            if int(each_total)==int(m):
                numbers.append(m)
                print(f"Running total: {total}")
                break
            else:
                print(f"Comparing: {m}!={each_total}")
        k+=1

for number in numbers:
    total+=number
print(f"Total: {total}")