t = int(input())

for _ in range(t):
    c, d = map(int, input().split())

    if (c + d) % 2 != 0:
        answer = -1
    else:
        if c == 0 and d == 0:
            answer = 0
        elif c == d:
            answer = 1
        else:
            answer = 2

    print(answer)
