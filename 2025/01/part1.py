#!/usr/bin/env python3

number=50
password=0

with open("input.txt") as fp:
    for line in fp:
        direction = line[0].strip()
        if direction =='L':
            number -= int(line[1:])
        elif direction =='R':
            number += int(line[1:])
        else:
            pass
        if number % 100 == 0:
            password += 1

print(password)