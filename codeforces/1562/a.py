import math

T = int(input())

for _ in range(T):
    l, r = map(int, input().split())

    if l <= math.ceil(r / 2):
        answer = math.ceil(r / 2) - 1
    else:
        answer = r - l

    print(answer)
