def check(a, b, c):
    if (a <= b and b <= c) or (a >= b and b >= c):
        return True
    else:
        return False


t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    w = n + n - 1

    x = 0
    if n >= 3:
        x += n - 2
        for i in range(1, n - 1):
            if check(a[i], a[i+1], a[i+2]):
                x -= 1

    y = 0
    if n >= 4:
        y += n - 3
        for i in range(1, n - 2):
            if check(a[i], a[i+1], a[i+2]):
                y -= 1
            elif check(a[i], a[i+1], a[i+3]):
                y -= 1
            elif check(a[i], a[i+2], a[i+3]):
                y -= 1
            elif check(a[i+1], a[i+2], a[i+3]):
                y -= 1

    answer = w + x + y
    print(answer)
