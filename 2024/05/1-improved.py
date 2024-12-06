# Advent of code
# Day 5
# Part 1 (but better)

# organize our lists
paragraphs=''
with open("example.txt", 'r') as fp:
    for line in fp:
        paragraphs+=line
two=paragraphs.split('\n\n')

#first list
page_order=[]
sublist=two[0].split('\n')
for i in range(len(sublist)): # first number
    page_order.append(sublist[int(i)].split('|'))
page_dict={}
for i in range(len(page_order)): # subsequent numbers
    tmp=[]
    for j in range(len(page_order)):
        if page_order[i][0]==page_order[j][0]:
            tmp.append(page_order[j][1])
    page_dict[page_order[i][0]]=tmp
print(page_dict)

# second lists: the update page numbers
update=[]
sublist=two[1].split('\n')
for i in range(len(sublist)):
    update.append(sublist[int(i)].split(','))

# Main code
total=0
for report in range(len(update)): # report is the list check and reorder
    good=True
    for page in range(len(update[report])): # page is the page currently being checked
        for val in page_dict: # val is the dictionary value to look against
            if update[report][page]==val:
                for right_page in page_dict[val]:
                    for page2 in range(len(update[report])):
                        if right_page==update[report][page2]:
                            print(update[report][page], update[report][page2])
                            print(page_dict[val])
                            if page2-page < 0:
                                good = False
    if good == True:
        total+=int(update[report][(len(update[report])-1)//2])
print(f"Total: {total}")  