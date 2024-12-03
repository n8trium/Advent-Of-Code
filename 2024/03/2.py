# Advent of code
# Day 3
# Part 2
import re

def do_or_dont(egg):
    pass


def searcher(bean):
    running_total = 0
    mult_list = (re.findall(r'mul\(\d{1,3},\d{1,3}\)', bean)) # search for each mul(#,#) instance allowing up to 3 digits
    for chunk in mult_list:
        sums=0 # reset the multiplying variable per loop
        splits=re.split(r"\(", chunk) # first split
        for var in splits: 
            splits_2=re.split(r"\)", var) # second split. Numbers are now stored in the first part of the list
        nums=splits_2[0].split(r",") # seperate the two numbers
        sums=int(nums[0])*int(nums[-1]) # multiply the two numbers
        running_total+=sums # add that value to the running total
    return(running_total)

with open("input.txt") as lines:
    total=0
    for line in lines: # iterate through each file
        total+=searcher(line)
print(f"Total: {total}") # print the total