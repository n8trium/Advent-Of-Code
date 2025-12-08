total = 0
with open("input.txt") as fp:
    for line in fp:
        length, width, height = map(int, line.strip().split("x"))
        bow = length*width*height
        wrap = 2*(length + width + height - max(length, width, height))
        total+=bow
        total+=wrap

print(total)