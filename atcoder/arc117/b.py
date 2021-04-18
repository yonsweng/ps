N = int(input())
A = map(int, input().split())

answer = 1
temp = 0

A = sorted(A)

for a in A:
    answer = (answer * (a - temp + 1)) % 1000000007
    temp = a

print(answer)
