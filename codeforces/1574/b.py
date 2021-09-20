t = int(input())
for _ in range(t):
    a, b, c, m = map(int, input().split())

    max_m = a + b + c - 3
    min_m = max(max(a, b, c) - (a + b + c + 1 - max(a, b, c)), 0)

    if min_m <= m and m <= max_m:
        print('YES')
    else:
        print('NO')
