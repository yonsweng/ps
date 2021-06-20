k = int(input())

for i in range(k):
    n, x, t = tuple(map(int, input().split()))
    m = t // x
    if n > m:
        answer = m * (n - m) + (m - 1) * m // 2
    else:
        answer = (n - 1) * n // 2
    print(max(0, answer))
