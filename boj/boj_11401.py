from sys import stdin

p = 1000000007


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % p
    return result


def power(x, y, p, m):
    if y in m:
        return m[y]
    if y == 0:
        return 1
    if y == 1:
        return x % p
    m[y] = (power(x, y // 2, p, m) ** 2) % p
    if y % 2 == 0:
        return m[y]
    m[y] = (m[y] * x) % p
    return m[y]


def main():
    n, k = map(int, stdin.readline().split())

    answer = factorial(n) * power(factorial(k), p - 2, p, {}) % p * power(factorial(n - k), p - 2, p, {}) % p
    print(answer)


if __name__ == "__main__":
    main()
