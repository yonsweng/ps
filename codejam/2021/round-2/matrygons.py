MAX = 1000000

T = int(input())
N = []
for x in range(1, T + 1):
    N.append(int(input()))

cnt = 0
divisors = [[] for _ in range(MAX + 1)]
for d in range(2, MAX + 1):
    for n in range(2 * d, MAX + 1, d):
        divisors[n].append(d)
        cnt += 1

print(cnt)
f = [0] * (MAX + 1)
f[2] = 1
g = [0] * (MAX + 1)
for n in range(3, MAX + 1):
    max_f, max_g = 1, 1
    for q in divisors[n]:
        max_f = max(max_f, f[n//q-1]+1)
        if q > 2:
            max_g = max(max_g, f[n//q-1]+1)
    f[n] = max_f
    g[n] = max_g


for x in range(1, T + 1):
    print(f'Case #{x}: {g[N[x-1]]}')
