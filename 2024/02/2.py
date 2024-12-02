# Advent of code
# Day 2
# Part 2

total_safe = 0 # our total subtracted from each list

def check_safe(testing):
    mark = 0 # badness checker
    for i, element in enumerate(testing[:-1]):
        a=abs(int(element)-int(testing[i+1]))
        if a < 1:
            mark+=1 # too small of a gap
        elif a > 3:
            mark+=1 # too large of a gap
        else:
            pass # passes
    if mark == 0:
        return True # all iterations passed
    else:
        return False # at least 1 iteration failed

with open("input.txt") as lines:
    for line in lines: # iterate through each file
        report_list=[]
        level_list = line.split(" ") # split and store the list
        level_list = [int(a.strip()) for a in level_list] # store each as a number
        report_list.append(level_list)

        for item in range(len(level_list)): # iterate through the reports
            report_list.append(level_list[:item]+level_list[item+1:]) # make the sublists and put them in a list of lists.
            # When one of these lists is good, we move to the next report (and it's offspring).

        for testing in report_list:
            if check_safe(testing)==True: # check for large gaps and repeating numbers
                if testing==sorted(testing): # of these check if it is ascending
                    total_safe+=1 # increment if ascending
                    break # Move to the next set of lists

                elif testing==sorted(testing, reverse=True): # of these check if it is descending
                    total_safe+=1 # increment if descending
                    break # Move to the next set of lists
            # if each list does not pass the above criteria, move on to the next in the series. 

print(f"Safe reports: {total_safe}")
