from sys import stdin


def read_input():
    k, x = map(int, stdin.readline().split())
    return k, x


def n_emotes(m, k):
    if m <= k:
        return m * (m + 1) // 2
    else:
        return k * (k + 1) // 2 + (m - k) * (3 * k - m - 1) // 2


def solve(k, x):
    low, high = 0, 2 * k - 1

    while low <= high:
        m = (low + high) // 2

        if n_emotes(m, k) >= x:
            high = m - 1
        else:
            low = m + 1

    return min(low, 2 * k - 1)


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
