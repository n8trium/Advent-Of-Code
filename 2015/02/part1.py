total = 0
with open("input.txt") as fp:
    for line in fp:
        length, width, height = map(int, line.strip().split("x"))
        s1 = 2*length*width
        s2 = 2*width*height
        s3 = 2*height*length
        gift = s1 + s2 + s3 + min(s1, s2, s3)//2
        total += gift

print(total)