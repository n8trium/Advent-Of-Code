# Advent of code
# Day 4
# Part 2
import re

def find_a(word_search):
    rows=len(word_search)
    columns=len(word_search[0])
    x_x=[]
    x_y=[]
    for i in range(rows-2): # don't need to check edges for A
        for j in range(columns-2): # don't need to check edges for A
            a = re.search("A", word_search[i+1][j+1])
            if a != None:
                x_x.append(i+1)
                x_y.append(j+1)
    return(x_x, x_y)

def find_let(word_search, x, y, letter):
    rows=len(word_search)
    columns=len(word_search[0])
    a = re.search(letter, word_search[x][y])
    if a != None:
        return(True)
    else:
        return(False)

def corner_check(puzzle, a_x, a_y):
    up_left=(a_x-1, a_y-1)
    up_right=(a_x+1, a_y-1)
    low_left=(a_x-1, a_y+1)
    low_right=(a_x+1, a_y+1)

    if find_let(puzzle, up_left[0], up_left[1], "S") == True:
        if find_let(puzzle, low_right[0], low_right[1], "M") == True:
            if find_let(puzzle, low_left[0], low_right[1], "S") == True:
                if find_let(puzzle, up_right[0], up_right[1], "M") == True:
                    return(True)
                else:
                    return(False)
            elif find_let(puzzle, low_left[0], low_right[1], "M") == True:
                if find_let(puzzle, up_right[0], up_right[1], "S") == True:
                    return(True)
                else:
                    return(False)
            else:
                return(False)
        else:
            return(False)
    elif find_let(puzzle, up_left[0], up_left[1], "M") == True:
        if find_let(puzzle, low_right[0], low_right[1], "S") == True:
            if find_let(puzzle, low_left[0], low_right[1], "S") == True:
                if find_let(puzzle, up_right[0], up_right[1], "M") == True:
                    return(True)
                else:
                    return(False)
            elif find_let(puzzle, low_left[0], low_right[1], "M") == True:
                if find_let(puzzle, up_right[0], up_right[1], "S") == True:
                    return(True)
                else:
                    return(False)
            else:
                return(False)
        else:
            return(False)

with open("input.txt") as lines:
    total=0
    matrix = []
    for line in lines: # iterate through each file
        row =[]
        for element in str(line).strip():
            row.append(str(element))
        matrix.append(row)
    x_0, y_0 = find_a(matrix)
    for a in range(len(x_0)):
        print(f"A found at {x_0[a]}, {y_0[a]}")
        if corner_check(matrix, x_0[a], y_0[a]) == True:
            print(f"Good: {x_0[a]}, {y_0[a]}")
            total+=1
        # else:
            # print(f"Bad A found at {x_0[a]}, {y_0[a]}")

print(f"Total: {total}")