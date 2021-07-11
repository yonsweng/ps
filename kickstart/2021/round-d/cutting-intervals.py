T = int(input())

for x in range(1, T + 1):
    N, C = map(int, input().split())

    A = []

    for i in range(N):
        L, R = map(int, input().split())

        A.append((L, 1))
        A.append((R, -1))

    A.sort()

    S = [0] * (10 ** 5 + 1)
    prev = 1
    curr = 0
    for i, a in A:
        S[curr] += i - prev - (1 if a == -1 else 0)
        if a == -1 and curr > 0:
            S[curr - 1] += 1
        curr += a
        prev = i

    y = N
    while C > 0 and N > 0:
        if S[N] > 0:
            k = min(C, S[N])
            C -= k
            y += k * N
        N -= 1

    print(f'Case #{x}: {y}')
