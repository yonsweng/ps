from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    b = [max(ai - i * k for i, ai in enumerate(a))]
    for i in range(1, n):
        b.append(b[-1] + k)

    ans = 0
    for i in range(n):
        ans += b[i] - a[i]

    print(ans)


if __name__ == "__main__":
    main()
