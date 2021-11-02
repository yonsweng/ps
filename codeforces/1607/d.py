from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().split()))
    c = stdin.readline().rstrip()
    return n, a, c


def solve(n, a, c):
    rods = []
    for i in range(n):
        if c[i] == 'B':
            if a[i] >= 1:
                left = 1
                right = min(n, a[i])
                rods.append((left, right))
        else:
            if a[i] <= n:
                left = max(1, a[i])
                right = n
                rods.append((left, right))

    if len(rods) < n:
        return 'NO'

    rods.sort()
    for i, rod in enumerate(rods, 1):
        if not (rod[0] <= i <= rod[1]):
            return 'NO'

    return 'YES'


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
