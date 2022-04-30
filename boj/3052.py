s = set()
for _ in range(10):
    a = int(input())
    remainder = a % 42
    s.add(remainder)
print(len(s))
