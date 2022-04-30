from sys import stdin, stdout

S = set()

R = set()
for i in range(1, 21):
    R.add(i)

M = int(stdin.readline())

for _ in range(M):
    splitted_line = stdin.readline().split()
    if len(splitted_line) == 1:
        operation = splitted_line[0]
    elif len(splitted_line) == 2:
        operation, x = splitted_line
        x = int(x)

    if operation == 'add':
        S.add(x)
        R.discard(x)
    elif operation == 'remove':
        S.discard(x)
        R.add(x)
    elif operation == 'check':
        stdout.write(str(1 if x in S else 0) + '\n')
    elif operation == 'toggle':
        if x in S:
            S.remove(x)
            R.add(x)
        else:
            S.add(x)
            R.remove(x)
    elif operation == 'all':
        for i in R:
            S.add(i)
        R.clear()
    elif operation == 'empty':
        for i in S:
            R.add(i)
        S.clear()
