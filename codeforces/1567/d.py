t = int(input())
for _ in range(t):
    s, n = map(int, input().split())
    p = 1
    while s >= p:
        p *= 10
    p //= 10
    answer = []
    for i in range(n-1):
        while s - p < n - (i + 1):
            p //= 10
        s -= p
        answer.append(p)
    answer.append(s)
    print(' '.join(map(str, answer)))
