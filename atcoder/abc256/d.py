from sys import stdin

A = [0] * 200001

N = int(input())
for _ in range(N):
    L, R = map(int, stdin.readline().split())
    A[L] += 1
    A[R] -= 1

S = []
cu = 0
start = 0
for i in range(1, 200001):
    prev_cu = cu
    cu += A[i]
    if prev_cu == 0 and cu > 0:
        start = i
    elif prev_cu > 0 and cu == 0:
        S.append((start, i))

for X, Y in S:
    print(X, Y)
