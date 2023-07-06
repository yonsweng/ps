from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    age, name = stdin.readline().split()
    arr.append((int(age), name))

arr.sort(key=lambda x: x[0])

for i in arr:
    print(i[0], i[1], flush=False)
