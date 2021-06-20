n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)

diff = [0] * (len(a) - 1)
for i in range(len(a) - 1):
    diff[i] = a[i+1] - a[i]

diff = sorted(diff)

answer = 1
for d in diff:
    if d > x:
        add = (d - 1) // x
        if k - add < 0:
            answer += 1
        else:
            k -= add

print(answer)
