from sys import stdin


def read_input():
    n, m = map(int, stdin.readline().split())
    s = stdin.readline().rstrip()
    return n, m, s


def solve(n, m, s):
    r, c = 0, 0
    left, right, bottom, top = 0, 0, 0, 0

    for si in s:
        if si == 'L':
            if right - (c - 1) >= m:
                break
            c -= 1
            left = min(left, c)
        elif si == 'R':
            if (c + 1) - left >= m:
                break
            c += 1
            right = max(right, c)
        elif si == 'D':
            if (r + 1) - top >= n:
                break
            r += 1
            bottom = max(bottom, r)
        else:
            if bottom - (r - 1) >= n:
                break
            r -= 1
            top = min(top, r)

    return str(1 - top) + ' ' + str(1 - left)


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
