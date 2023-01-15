from sys import stdin

ss = stdin.readline().rstrip()

s = ["#"]
for _, c in enumerate(ss):
    s.append(c)
    s.append("#")

d = [0] * len(s)
p = 0
v = 0
for i in range(1, len(d)):
    if i <= v:
        d[i] = min(d[2 * p - i], v - i)
    while (
        i - d[i] - 1 >= 0
        and i + d[i] + 1 < len(d)
        and s[i - d[i] - 1] == s[i + d[i] + 1]
    ):
        d[i] += 1
    if i + d[i] > v:
        p = i
        v = i + d[i]

answer = 0
for i, di in enumerate(d):
    if i % 2 == 0:
        answer += di // 2
    else:
        answer += (di + 1) // 2

print(answer)
