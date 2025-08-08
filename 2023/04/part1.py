total=0

with open("input.txt", "r") as fp:
    inputs = [line.rstrip() for line in fp]
    #print(inputs)

for line in inputs:
    per_card=0
    winners, nums = line.split(":")[-1].split("|")
    winners = list(filter(None, winners.strip().split(" ")))
    nums= list(filter(None, nums.strip().split(" ")))
    for i in winners:
        for j in nums:
            if i==j:
                if per_card==0:
                    per_card+=1
                else:
                    per_card*=2
                break
    total+=per_card
print(total)