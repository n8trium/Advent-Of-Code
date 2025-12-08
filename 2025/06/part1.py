inputlines = [line.rstrip() for line in open('input.txt')]

operators=inputlines[-1].split()
problems=[]
for i in range(len(inputlines)-1):
    problems.append(list(map(int, inputlines[i].split())))

total=0
for op in range(len(operators)):
    answer = problems[0][op]
    if operators[op] == '*':
        for value in range(1, len(problems)):
            answer *= problems[value][op]
    else:
        for value in range(1, len(problems)):
            answer += problems[value][op]
    total+=answer
print(total)