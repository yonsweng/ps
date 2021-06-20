n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

ab = sorted(ab, key=lambda c: c[1])

answer = 0
cnt = 0
i = 0
j = n - 1
while i < n:
    if cnt >= ab[i][1]:
        cnt += ab[i][0]
        answer += ab[i][0]
        ab[i][0] = 0
        i += 1
    else:
        q = min(cnt - ab[i][1], ab[j][0])
        cnt += q
        answer += q * 2
        ab[j][0] -= q
        if ab[j][0] == 0:
            j -= 1

print(answer)
