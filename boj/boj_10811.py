n, m = map(int, input().split())
arr = list(range(n + 1))
for _ in range(m):
    a, b = map(int, input().split())
    arr[a:b + 1] = arr[a:b + 1][::-1]
print(*arr[1:])
