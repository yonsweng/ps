a, b = map(int, input().split())

for d in range(b // 2, 0, -1):
    if a <= (b // d - 1) * d:
        print(d)
        break
