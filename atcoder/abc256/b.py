N = int(input())
A = list(map(int, input().split()))

for i in range(N-2, -1, -1):
    A[i] += A[i+1]

cnt = 0
for Ai in A:
    if Ai > 3:
        cnt += 1

print(cnt)
