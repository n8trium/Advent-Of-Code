total=0

with open("input.txt", "r") as fp:
    inputs = [line.rstrip() for line in fp]

last_card=int(inputs[-1].split(":")[0].split(" ")[-1])
game_cards={}
for i in range(1, last_card+1):
    game_cards[i]=1

for line in inputs:
    card_gen=0
    id=int(line.split(":")[0].split(" ")[-1])
    winners, nums = line.split(":")[-1].split("|")
    winners = list(filter(None, winners.strip().split(" ")))
    nums= list(filter(None, nums.strip().split(" ")))
    for i in winners:
        for j in nums:
            if i==j:
                card_gen+=1
    for k in range(1, card_gen+1):
        new_id=id+k
        if new_id <= last_card:
            game_cards[new_id]+=game_cards[id]
    
for i in game_cards:
    total+=game_cards[i]
print(total)