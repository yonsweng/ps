T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    answer = []
    for c in s:
        if c == 'U':
            answer.append('D')
        elif c == 'D':
            answer.append('U')
        else:
            answer.append(c)
    print(''.join(answer))
