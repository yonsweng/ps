n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a | b
a = c.difference(a)
b = c.difference(b)
c = a | b
print(*c)