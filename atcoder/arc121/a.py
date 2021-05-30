N = int(input())

d = []

for i in range(N):
    x, y = map(int, input().split())
    d.append((i, x, y))

d = sorted(d, key=lambda t: t[1])

diffs = []

index = (d[0][0], d[N-1][0]) if d[0][0] < d[N-1][0] else (d[N-1][0], d[0][0])
diff = d[N-1][1] - d[0][1]
diffs.append((index, diff))

index = (d[0][0], d[N-2][0]) if d[0][0] < d[N-2][0] else (d[N-2][0], d[0][0])
diff = d[N-2][1] - d[0][1]
diffs.append((index, diff))

index = (d[1][0], d[N-1][0]) if d[1][0] < d[N-1][0] else (d[N-1][0], d[1][0])
diff = d[N-1][1] - d[1][1]
diffs.append((index, diff))

d = sorted(d, key=lambda t: t[2])

index = (d[0][0], d[N-1][0]) if d[0][0] < d[N-1][0] else (d[N-1][0], d[0][0])
diff = d[N-1][2] - d[0][2]
diffs.append((index, diff))

index = (d[0][0], d[N-2][0]) if d[0][0] < d[N-2][0] else (d[N-2][0], d[0][0])
diff = d[N-2][2] - d[0][2]
diffs.append((index, diff))

index = (d[1][0], d[N-1][0]) if d[1][0] < d[N-1][0] else (d[N-1][0], d[1][0])
diff = d[N-1][2] - d[1][2]
diffs.append((index, diff))

diffs = sorted(diffs, key=lambda t: t[1], reverse=True)

if diffs[0][0] == diffs[1][0]:
    answer = diffs[2][1]
else:
    answer = diffs[1][1]

print(answer)
