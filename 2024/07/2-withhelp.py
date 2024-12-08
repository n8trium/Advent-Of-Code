# Advent of Code
# 2024
# Day 7
# Part 2: with help (so it could finish in a reasonable timeframe)
# n8trium

total=0
data = [list(map(int, line.replace(':','').split())) for line in open('input.txt')]

def checking(calibration_result, values):
    if len(values)==1:
        return(values[0]==calibration_result)
    
    last=values[-1]

    if calibration_result % last == 0:
        div_check=checking(calibration_result // last, values[:-1])
    else:
        div_check=False
    
    scaling = 1
    while scaling<=last:
        scaling *= 10
    if (calibration_result - last) % scaling == 0:
        cat_check=checking((calibration_result-last)//scaling, values[:-1])
    else:
        cat_check=False
    
    sub_check=checking(calibration_result - last, values[:-1])
    return div_check or sub_check or cat_check

for line in data:
    result = line[0]
    rest= line[1:]
    # print(rest)
    if checking(result, rest) == True:
        print(f"Adding: {result}")
        total+=result
    
print(f"Total: {total}")
