from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    return n, a


def solve(n, a):
    answer = 1


    for i in range(1, n):
        for s in range(0, n - 1):
            ds = [(a[k] - a[s]) // j for j, k in enumerate(range(s + i, n, i), 1) if (a[k] - a[s]) % j == 0]
            for d in ds:
                cnt = 1

                expected = a[s] + d
                for k in range(s + i, n, i):
                    if expected < -100 or expected > 100:
                        break
                    if a[k] == expected:
                        cnt += 1
                    expected += d

                answer = max(answer, cnt)

    return n - answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
