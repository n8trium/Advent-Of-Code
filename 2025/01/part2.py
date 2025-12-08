#!/usr/bin/env python3

number=50
password=0

with open("input.txt") as fp:
    for line in fp:
        direction = line[0].strip()
        scalar = int(line[1:].strip())
        if direction == "L":
            number -= scalar
        elif direction == "R":
            if number == 0:
                password += 1
            number += scalar
        
        while number < 0 or number > 99: # outside dial
            if number < 0:
                number += 100
                password += 1
            elif number > 100:
                number -= 100
                password += 1
            elif number == 100:
                number -= 100
if number == 0:
    password+=1
print(password)