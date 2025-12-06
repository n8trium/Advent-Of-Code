inputlines = [line.rstrip('\n') for line in open('input.txt')]
operators=list(reversed(inputlines[-1].split()))
problems=[]
numbers=[]
for y in reversed(range(len(inputlines[0]))):
    print(y)
    number=""
    for x in (range(len(inputlines)-1)):
        number+=inputlines[x][y]
    if number.strip()=='':
        number=""
        problems.append(numbers)
        numbers=[]
    else:
        numbers.append(int(number.strip()))
problems.append(numbers)

total=0
for op in range(len(operators)):
    answer = problems[op][0]
    if operators[op] == '*':
        for value in range(1, len(problems[op])):
            answer *= problems[op][value]
    else:
        for value in range(1, len(problems[op])):
            answer += problems[op][value]
    total+=answer
print(total)