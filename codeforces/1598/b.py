from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    g = []
    for _ in range(n):
        g.append(list(map(int, stdin.readline().split())))
    return n, g


def solve(n, g):
    for day1 in range(5):
        for day2 in range(5):
            if day1 != day2:
                a, b, c = 0, 0, 0
                for h in g:
                    if h[day1] == 1 and h[day2] == 1:
                        c += 1
                    elif h[day1] == 1:
                        a += 1
                    elif h[day2] == 1:
                        b += 1
                if a + b + c == n and a + c >= n // 2 and b + c >= n // 2:
                    return 'YES'
    return 'NO'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
