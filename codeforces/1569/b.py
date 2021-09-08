t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    n_twos = 0
    two_indices = []
    for i in range(n):
        if s[i] == '2':
            n_twos += 1
            two_indices.append(i)

    if n_twos == 1 or n_twos == 2:
        print('NO')
        continue

    print('YES')

    m = [['='] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = 'X'

    for i in range(len(two_indices)):
        m[two_indices[i]][two_indices[(i+1)%len(two_indices)]] = '+'
        m[two_indices[(i+1)%len(two_indices)]][two_indices[i]] = '-'

    for l in m:
        print(''.join(l))
