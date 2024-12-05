# Advent of code
# Day 5
# Part 1

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
with open("input.txt", 'r') as fp:
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

# check each list
running_total=0
# loop over the updates
for set in range(len(update)):
    # loop over the pages in each update
    passing_passes=0
    print(f"\n{update[set]}")
    for page in range(len(update[set])):
        print(f"Checking: {update[set][page]}")
        rule,rule_index=num_search(update[set][page], page_order)
        passes=0 #counts any passes, indicates when to find the middle number
        for each in range(len(rule)):
            # print(f"Rule: {rule[each]},{rule_index[each]}")
            fails=0 #counts fail, our exit variable
            # check if the number was high page or low page
            if rule_index[each] == 0:
                low=page
                high=rule_check(page_order[rule[each]][1], update[set])
                # print(f"Rule: {rule[each]},{rule_index[each]}")
                # print(page_order[each][1], update[set])
            else:
                low=rule_check(page_order[rule[each]][0], update[set])
                high=page
            # now for the mess
            if high == None:
                # print(f"No num: {page_order[rule[each]][0]}|{page_order[rule[each]][1]}")
                passes+=1
                pass
            elif low == None:
                # print(f"No num: {page_order[rule[each]][0]}|{page_order[rule[each]][1]}")
                passes+=1
                pass
            elif high-low < 0:
                # print(f"Fail: {page_order[rule[each]][0]}|{page_order[rule[each]][1]}")
                fails+=1
                break
            else:
                passes+=1
                # print(f"Pass: {page_order[rule[each]][0]}|{page_order[rule[each]][1]}", passes)   
            if passes==len(rule):
                passing_passes+=1
                if passing_passes==len(update[set]):
                    print("\nGood set: ", update[set])
                    middle=(len(update[set])-1)//2
                    print(f"Middle #: {update[set][middle]}\n")
                    running_total+=int(update[set][middle])      
        if fails>0:
            fails=0
            break
        else:
            continue  # Continue if the inner loop wasn't broken
total=running_total
print(f"Total: {total}")
