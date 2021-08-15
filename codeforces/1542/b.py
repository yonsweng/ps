t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    yes = False
    ak = 1
    while ak <= n:
        if (n - ak) % b == 0:
            yes = True
            break
        if a == 1:
            break
        ak *= a

    if yes:
        print('Yes')
    else:
        print('No')
