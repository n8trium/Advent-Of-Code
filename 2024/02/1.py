# Advent of code
# Day 2
# Part 1

safe = 0 # our total subtracted from each list

def check_safe(level_list):
    mark = 0 # badness checker
    for i, element in enumerate(level_list[:-1]):
        a=abs(int(element)-int(level_list[i+1]))
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
        level_list = line.split(" ") # split and store the list
        level_list = [int(a.strip()) for a in level_list] # store each as a number
        if check_safe(level_list)==True: # check for large gaps and repeating numbers
            if level_list==sorted(level_list): # of these check if it is ascending
                safe+=1 # increment if ascending
                # print(f"Ascend: {level_list}")
            elif level_list==sorted(level_list, reverse=True): # of these check if it is descending
                safe+=1 # increment if descending
                # print(f"Descend: {level_list}")
            else:
                pass
                # print(f"Neither: {level_list} and {sorted(level_list)}")            
print(f"Safe reports: {safe}")
