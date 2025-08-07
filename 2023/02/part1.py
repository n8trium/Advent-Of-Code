total=0


def color_check(color_strings):
    maxes=[12, 13, 14] #RGB order
    color_codes=['r', 'g', 'b']
    for color_string in color_strings:
        #print(color_string)
        number, current_color=color_string.split(" ")
        for i in range(len(color_codes)):
            if current_color[0]==color_codes[i]:
                if maxes[i]<int(number):
                    return(False)
                else:
                    if color_string==color_strings[-1]:
                        return(True)

with open("input.txt") as fp:
    for line in fp:
        success=True
        game_id, games = line.strip().split(":")
        game_id=int(game_id.split(" ")[-1])
        trials=games.split("; ")
        for i in range(len(trials)):
            colors=trials[i].split(",")
            new_colors = [s.strip() for s in colors]
            success=color_check(new_colors)
            if success!=True:
                print(f"{game_id}: Not Possible!")
                break
            if i==len(trials)-1:
                print(f"{game_id}: Possible!")
                total+=game_id
print(f"Total: {total}")