n, m = map(int, input().split())

l = n - m

l, m = min(l, m), max(l, m)

answer = 1

for i in range(n, m, -1):
    answer *= i

for i in range(2, l + 1):
    answer //= i

print(answer)
