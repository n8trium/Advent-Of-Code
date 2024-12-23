import re
#variables
row=[]
dir = 'N'
guard='^'
count=1
#file stuff
maze = [line.strip() for line in open('example.txt')]
print(maze)

#maze coords: maze[y][x]
def find_coords(pattern, the_map):
    for y in range(len(the_map)):
        for x in range(len(the_map[y])):
            if pattern==the_map[y][x]:
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

def check_square(x, y, squares, dir, counter):
    print(len(squares[y]), len(squares))
    while True:
        if x<0 or x>len(squares[0])-1 or y<0 or y>len(squares)-1:
            print("Out of maze!")
            return(counter, squares)
        else:
            square=squares[y][x]
            match square:
                case '^':
                    print("Start square!")
                    if dir=='N' and counter>5:
                            counter=False
                            return(counter, squares)
                    x, y = move(x, y, dir)
                    pass
                case '.':
                    counter+=1
                    print(f"Counting: {counter}")
                    squares[y]=squares[y][:x] + 'X' + squares[y][x + 1:]
                    x, y = move(x, y, dir)
                    pass
                case 'X':
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
count, new_maze = check_square(x_0, y_0, maze, dir, count)
loops=0
#p2
for row in range(len(new_maze)):
    for column in range(len(new_maze[row])):
        if new_maze[row][column-1]=='^':
            pass
        elif new_maze[row][column]=='X':
            new_maze[row]=new_maze[row][:column] + 'O' + new_maze[row][column + 1:]
            for y in range(len(maze)):
                print(new_maze[y])
            print('\n')
            #count, junk=check_square(x_0, y_0, new_maze, dir, count)
            if count==False:
                loops+=1
            new_maze[row]=new_maze[row][:column] + 'X' + new_maze[row][column + 1:]
#for y in range(len(maze)):
#        print(new_maze[y])
print(f"Loops: {loops}")