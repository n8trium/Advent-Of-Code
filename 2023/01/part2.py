total=0
STR_DIGITS=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
with open("input.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            else:
                for si, ss in enumerate(STR_DIGITS):
                    if line[i:].startswith(ss):
                        digits.append(str(si+1))
        total += int(digits[0] + digits[-1])
print(f"Total: {total}")