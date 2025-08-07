total=0

def color_check(game):
    color_codes=['r', 'g', 'b']
    rgb=[0,0,0]
    for i in range(len(game)):
        trial=game[i].strip().split(", ")
        #print(trial)
        for j in range(len(trial)):
            number, new_color=trial[j].strip().split(" ")
            for y in range(len(color_codes)):
                if new_color[0]==color_codes[y]:
                    if int(number) > rgb[y]:
                        rgb[y]=int(number)
    return(rgb[0]*rgb[1]*rgb[2])

with open("input.txt") as fp:
    for line in fp:
        success=True
        game_id, games = line.strip().split(":")
        game_id=int(game_id.split(" ")[-1])
        trials=games.split("; ")
        total+=color_check(trials)
print(f"Total: {total}")