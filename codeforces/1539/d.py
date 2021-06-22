n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

ab = sorted(ab, key=lambda c: c[1])

total = sum([c[0] for c in ab])
answer = 0
cnt = 0
i = 0
j = n - 1
while cnt < total:
    if cnt >= ab[i][1]:
        cnt += ab[i][0]
        answer += ab[i][0]
        ab[i][0] = 0
        i += 1
    else:
        q = min(ab[i][1] - cnt, ab[j][0])
        cnt += q
        answer += q * 2
        ab[j][0] -= q
        if ab[j][0] == 0:
            j -= 1

print(answer)
