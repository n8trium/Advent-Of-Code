# Advent of code
# Day 5
# Part 2

# Finds the indexes of numbers
def num_search(num, rules):
    x_list=[]
    y_list=[]
    # check each rule
    for x in range(len(rules)):
        # look for a number in each rule
        for y in range(len(rules[x])):
            if rules[x][y]==num:
                x_list.append(x) # adds the rule itself
                y_list.append(y) # adds the index of that number in the rule
    return(x_list, y_list)

def rule_check(num, page_list):
    for pos in range(len(page_list)):
        if page_list[pos]==num:
            # print(num, page_list)
            return(pos)

# organize our lists
paragraphs=''
with open("example.txt", 'r') as fp:
    for line in fp:
        paragraphs+=line
two=paragraphs.split('\n\n')

#first list
page_order=[]
sublist=two[0].split('\n')
for i in range(len(sublist)):
    page_order.append(sublist[int(i)].split('|'))

# second lists: the update page numbers
update=[]
sublist=two[1].split('\n')
for i in range(len(sublist)):
    update.append(sublist[int(i)].split(','))

organized_list=[]
# iterate over the rules
while len(page_order)>2:
    infini_breaker=0
    print(f"{page_order}")
    for i in range(len(page_order)):
        infini_breaker+=1
        r_count=0
        storage=[]
        for j in range(len(page_order)):
            if page_order[i][0]==page_order[j][1]:
                print(f"Rule fail: {page_order[j][0]}|{page_order[j][1]}")
                r_count+=1 # means that this number is to the right of another number.
                storage=[]
            if page_order[i][0]==page_order[j][0]:
                # print(f"Rule {j} stored.")
                storage.append(j) # notes all positions of rules containing the # at i
    if r_count==0: # Current leftmost #
        infini_breaker=0
        organized_list.append(page_order[i][0])
        print(organized_list)
        k=len(storage)-1
        while k >= 0:
            del page_order[storage[k]]
            print(k)
            k-=1
        print(organized_list, page_order)
    if infini_breaker>2*len(page_order):
        print("Breaking loops")
        print(organized_list)
        break
organized_list.append(page_order[0][0])
organized_list.append(page_order[0][1])
print(organized_list)
