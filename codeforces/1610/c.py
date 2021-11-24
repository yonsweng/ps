from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    a, b = [], []
    for _ in range(n):
        ai, bi = map(int, stdin.readline().split())
        a.append(ai)
        b.append(bi)
    return n, a, b


def ok(x, a, b):
    cnt = 0
    for i, (ai, bi) in enumerate(zip(a, b), 1):
        if x - 1 - ai <= cnt <= bi:
            cnt += 1
            if cnt >= x:
                return True
    return False


def solve(n, a, b):
    # search the maximum x in [low, high)
    max_x = 0
    low, high = 1, n + 1
    while low < high:
        x = (low + high) // 2
        if ok(x, a, b):
            max_x = x
            low = x + 1
        else:
            high = x

    return max_x


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
