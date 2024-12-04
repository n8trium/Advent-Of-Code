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

def find_next_letter(word_search, x_coord, y_coord, letter="M", direction=0):
    rows=len(word_search)
    columns=len(word_search[0])
    x_pos=[]
    y_pos=[]
    dir_list=[]
    a=None
    if int(direction)==0:
        for i in range(0,3):
            for j in range (0,3):
                x_2=int(x_coord)+int(i)-1
                y_2=int(y_coord)+int(j)-1
                if x_2 or y_2 < 0:
                    print("a")
                    pass
                elif x_2 > columns:
                    print("b")
                    pass
                elif y_2 > rows:
                    print("c")
                    pass
                else:
                    a = re.search(str(letter), word_search[x_2][y_2])
                    print(a)
                if a != None:
                    x_pos.append(x_2)
                    y_pos.append(y_2)
                    print(x_coord, y_coord, x_pos[-1], y_pos[-1])
                    dir_list.append(direction_finder(x_coord, x_pos[-1], y_coord, y_pos[-1]))
        return(x_pos, y_pos, dir_list)
    
    # if direction!=0:
    #    for i in range(int(x_coord), int(x_coord)-1):
    #        for j in range(int(y_coord)-1, int(y_coord)-1):
    #            a = re.search(str(letter), word_search[i][j])
    #            if a != None:
    #                x_pos.append(i)
    #                y_pos.append(j)
    #                dir_list.append(direction_finder(x_coord, x_pos[-1], y_coord, y_pos[-1]))
    #    return(x_pos, y_pos, dir_list)

with open("example.txt") as lines:
    matrix = []
    for line in lines: # iterate through each file
        row =[]
        for element in str(line).strip():
            row.append(str(element))
        matrix.append(row)
    x_1, y_1 = find_x(matrix)
    for i in range(len(x_1)):
        x_2, y_2, dir_list = find_next_letter(matrix, x_1[i], y_1[i], "M", 0)
        print(f"X found at {x_1[i]}, {y_1[i]}")
        print(x_2, y_2, dir_list)

        
        
