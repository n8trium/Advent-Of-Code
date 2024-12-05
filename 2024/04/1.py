# Advent of code
# Day 4
# Part 1
import re

def direction_finder(x_1, x_2, y_1, y_2):
    x_dif=int(x_2)-int(x_1)
    y_dif=int(y_2)-int(y_1)
    if x_dif==-1:
        if y_dif==-1:
            return(8) # NorthWest
        elif y_dif==0:
            return(7) # West
        if y_dif==1:
            return(6) # SouthWest
    elif x_dif==0:
        if y_dif==-1:
            return(1) # North
        elif y_dif==0:
            return(0) # Center
        if y_dif==1:
            return(5) # South
    elif x_dif==1:
        if y_dif==-1:
            return(2) # NorthEast
        elif y_dif==0:
            return(3) # East
        if y_dif==1:
            return(4) # SouthEast

def direction_reverser(dir):
    dir=int(dir)
    match dir:
        case 1: # North
            x_dir,y_dir=0,-1
        case 2: # NorthEast
            x_dir,y_dir=1,-1
        case 3: # East
            x_dir,y_dir=1,0
        case 4: # SouthEast
            x_dir,y_dir=1,1
        case 5: # South
            x_dir,y_dir=0,1
        case 6: # SouthWest
            x_dir,y_dir=-1,1
        case 7: # West
            x_dir,y_dir=-1,0
        case 8: # NorthWest
            x_dir,y_dir=-1,-1
        case _: # Center
            x_dir,y_dir=0,0
    return(x_dir, y_dir)

def find_x(word_search):
    rows=len(word_search)
    columns=len(word_search[0])
    x_x=[]
    x_y=[]
    for i in range(rows):
        for j in range(columns):
            a = re.search("X", word_search[i][j])
            if a != None:
                x_x.append(i)
                x_y.append(j)
    return(x_x, x_y)

def find_next_letter(word_search, x_0, y_0, letter="M", direction=0):
    rows=len(word_search)
    columns=len(word_search[0])
    x_pos=[]
    y_pos=[]
    dir_list=[]
    if int(direction)==0:
        for i in range(0,3):
            x_1=x_0+i-1
            if 0<=x_1<rows:
                for j in range (0,3):
                    y_1=y_0+j-1
                    if 0<=y_1<columns:
                        if letter==str(word_search[x_1][y_1]):
                            print(f"{letter} found at {x_1}, {y_1}")
                            x_pos.append(x_1)
                            y_pos.append(y_1)
                            dir_list.append(direction_finder(x_0, x_1, y_0, y_1))
        return(x_pos, y_pos, dir_list)
    
    if direction!=0:
        x_1, y_1 = direction_reverser(direction)
        x_1+=int(x_0)
        y_1+=int(y_0)
        if 0<=x_1<rows:
            if 0<=y_1<columns:
                if letter==str(word_search[x_1][y_1]):
                    print(f"{letter} found at {x_1}, {y_1}")
                    if letter != "S":
                        x_pos.append(x_1)
                        y_pos.append(y_1)
                        return(x_pos, y_pos, direction)
                    else:
                        return(int(1))

with open("input.txt") as lines:
    total=0
    matrix = []
    for line in lines: # iterate through each file
        row =[]
        for element in str(line).strip():
            row.append(str(element))
        matrix.append(row)
    x_0, y_0 = find_x(matrix)
    for i in range(len(x_0)):
        print(f"X found at {x_0[i]}, {y_0[i]}")
        if find_next_letter(matrix, x_0[i], y_0[i], "M", 0) != None:
            x_1_list, y_1_list, dir_list = find_next_letter(matrix, x_0[i], y_0[i], "M", 0)
            for x, y, dir in zip(x_1_list, y_1_list, dir_list):
                if find_next_letter(matrix, x, y, "A", dir) != None:
                    x_2, y_2, dir = find_next_letter(matrix, x, y, "A", dir)
                    a=find_next_letter(matrix, x_2[0], y_2[0], "S", dir)
                    if a==1:
                        total+=int(a)

print(f"Total: {total}")