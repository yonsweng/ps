from sys import stdin


def read_input():
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    return n, k, a


def solve(n, k, a):
    if n == 1:
        return max(a[0] - k, 0)

    answer = 10 ** 10

    a.sort(reverse=True)

    s = [a[0] - a[-1]]
    for ai in a[1:-1]:
        s.append(s[-1] + (ai - a[-1]))

    p = 0
    q = n - 1
    k_ = sum(a) - k
    while q > 0:
        while q >= 0 and (s[q-1] if q > 0 else 0) + p * q >= k_ - p:
            answer = min(answer, p + q)
            q -= 1
        if q >= 0:
            p += max(1, (k_ - (s[q-1] if q > 0 else 0) + q) // (q + 1) - p)

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
