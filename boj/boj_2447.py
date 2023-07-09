n = int(input())

# k = log3(n)
k = 0
while n != 1:
    n //= 3
    k += 1

s = [["*"]]

for _ in range(k):
    m = len(s)
    t = [[" " for _ in range(m * 3)] for _ in range(m * 3)]
    for i in range(m):
        for j in range(m):
            for x in range(3):
                for y in range(3):
                    t[i * 3 + x][j * 3 + y] = s[i][j] if x != 1 or y != 1 else " "
    s = t

for i in range(len(s)):
    print("".join(s[i]), flush=False)
