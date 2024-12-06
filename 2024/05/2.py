# Advent of code
# Day 5
# Part 2

# organize our input into two lists
paragraphs=''
with open("input.txt", 'r') as fp:
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
print(page_dict) # Our dict!

# second lists: the update page numbers
update=[]
sublist=two[1].split('\n')
for i in range(len(sublist)):
    update.append(sublist[int(i)].split(','))

# Main code
total=0
loop_count=0
good_count=0
report_check=False
while report_check==False:
    for report in range(len(update)): # report is the list check and reorder
        good=True
        print(update[report])
        for page in range(len(update[report])): # page is the page currently being checked
            for left_page in page_dict: # left_page is the dictionary value to look against
                if update[report][page]==left_page:
                    for right_page in page_dict[left_page]:
                        for page2 in range(len(update[report])):
                            if right_page==update[report][page2]:
                                # print(update[report][page], update[report][page2])
                                # print(page_dict[left_page])
                                if page2-page < 0:
                                    good = False
                                    # print(f"{left_page}|{right_page}")
                                    print(f"Swapping {left_page}|{right_page} in {update[report]} aka p.{page} and p.{page2}")
                                    update[report][page], update[report][page2] = update[report][page2], update[report][page]
                                    print(f"New Report: {update[report]}")
        if good == True:
            if loop_count==0:
                print(f"Removing {update[report]}")
                for i in range(len(update[report])):
                    update[report][i]=0
            else:
                good_count+=1
        # print(update[report])
        # total+=int(update[report][(len(update[report])-1)//2])
        if good == False:
            print(f"Fixing {update[report]}")
    loop_count+=1
    if good_count==len(update):
        report_check=True
    else:
        good_count=0
# print(update)
for report in range(len(update)):
    total+=int(update[report][(len(update[report])-1)//2])
print(f"Total: {total}")