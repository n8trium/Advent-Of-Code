total=0


def color_check(color_strings):
    maxes=[12, 13, 14] #RGB order
    color_codes=['r', 'g', 'b']
    for color_string in color_strings:
        print(color_string)
        number=int(color_string[0])
        current_color=color_string[2]
        for i in range(len(color_codes)):
            if current_color==color_codes[i]:
                if maxes[i]<number:
                    print("fail?")
                    return(False)
                else:
                    print(f"{i}, {len(color_strings)}")
                    if i==len(color_strings)-1:
                        return(True)

with open("example01.txt") as fp:
    for line in fp:
        success=True
        game_id, games = line.strip().split(":")
        game_id=int(game_id.split(" ")[-1])
        print(f"\nGame: {game_id}")
        trials=games.split("; ")
        for i in range(len(trials)):
            colors=trials[i].split(",")
            new_colors = [s.strip() for s in colors]
            success=color_check(new_colors)
            print(f"{game_id}: {success}")
            if success!=True:
                break
            if i==len(trials)-1:
                print(f"{game_id}: Success!")
                total+=game_id
print(f"Total: {total}")