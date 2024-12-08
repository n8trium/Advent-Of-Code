import re
#variables
hash_map=[]
row=[]
dir = 'N'
guard='^'
#file stuff
maze = [line.strip() for line in open('input.txt')]
print(maze)

#maze coords: maze[y][x]
def find_coords(pattern, the_maze):
    for y in range(len(the_maze)):
        for x in range(len(the_maze[y])):
            if pattern==the_maze[y][x]:
                return(x, y)

def turning(dir):
    match dir:
        case 'N':
            print("Turning")
            return('E')
        case 'E':
            print("Spinning")
            return('S')
        case 'S':
            print("Floating")
            return('W')
        case 'W':
            print("Flying")
            return('N')

def check_square(x, y, squares, dir, the_map):
    counter=0
    print(len(squares[y]), len(squares))
    while True:
        counter+=1
        print(counter)
        if x<0 or x>len(squares[0])-1 or y<0 or y>len(squares)-1:
            print("Out of maze!")
            return(the_map, squares)
        else:
            square=squares[y][x]
            match square:
                case '^':
                    the_map.append([x, y, dir])
                    print("Start square!")
                    if dir=='N':
                        if counter!=1:
                            counter=False
                            return(counter, squares)
                    x, y = move(x, y, dir)
                    pass
                case '.':
                    the_map.append([x, y, dir])
                    print(f"Counting: {counter}")
                    squares[y]=squares[y][:x] + 'X' + squares[y][x + 1:]
                    x, y = move(x, y, dir)
                    pass
                case 'X':
                    the_map.append([x, y, dir])
                    x, y = move(x, y, dir)
                    pass
                case '#':
                    match dir:
                        case 'N':
                            y+=1
                            dir='E'
                            pass
                        case 'E':
                            x-=1
                            dir='S'
                            pass
                        case 'S':
                            y-=1
                            dir='W'
                            pass
                        case 'W':
                            x+=1
                            dir='N'
                            pass
                    #print(f"New dir: {dir}")
                    x, y = move(x, y, dir)
                    pass
                case _:
                    print('New path!')
                    match dir:
                        case 'N':
                            y+=1
                            dir='E'
                            pass
                        case 'E':
                            x-=1
                            dir='S'
                            pass
                        case 'S':
                            y-=1
                            dir='W'
                            pass
                        case 'W':
                            x+=1
                            dir='N'
                            pass
                    #print(f"New dir: {dir}")
                    x, y = move(x, y, dir)
                    pass
            #for maze_line in range(len(squares)):
            #            print(squares[maze_line])
            #print(x, y)
        if counter>100000:
            return(True, True)
def move(x, y, direction):
    match direction:
        case 'N':
            print("N")
            y-=1
            pass
        case 'E':
            print("E")
            x+=1
            pass
        case 'S':
            print("S")
            y+=1
            pass
        case 'W':
            print("W")
            x-=1
            pass
    return(x, y)

x_0, y_0 = find_coords(guard, maze)
hash_map, new_maze = check_square(x_0, y_0, maze, dir, hash_map)
print(hash_map)
print(len(hash_map))
loops=0
#p2
for spot in range(1, len(hash_map)):
    x_a=hash_map[spot-1][0]
    y_a=hash_map[spot-1][1]
    z_a=turning(hash_map[spot-1][2])
    x_b=hash_map[spot][0]
    y_b=hash_map[spot][1]
    z_b=hash_map[spot][2]
    if new_maze[y_b][x_b]=='^':
            pass
    elif new_maze[y_b][x_b]=='X':
        new_maze[y_b]=new_maze[y_b][:x_b] + 'O' + new_maze[y_b][x_b + 1:]
        #for y in range(len(maze)):
        #    print(new_maze[y])
        print('\n')
        #count, junk = check_square(x_a, y_a, maze, z_a, hash_map)
        #if count == False:
        #    pass
        #    loops+=1
        #if count == True:
        #    loops+=1
        new_maze[y_b]=new_maze[y_b][:x_b] + 'X' + new_maze[y_b][x_b + 1:]
print(f"Loops: {loops}")
print(len(hash_map))