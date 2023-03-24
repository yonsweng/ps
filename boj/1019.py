from sys import stdin, stdout


def count(n, k):
    cnt = 0

    p = 1
    while p <= n:
        if (k == 0 and n // p < 10) or n // p < k:
            break

        start = p if k == 0 else 0

        if k == n // p % 10:
            end = n // p // 10 * p + n % p
        elif k > n // p % 10:
            end = (n // p // 10 - 1) * p + p - 1
        else:
            end = n // p // 10 * p + p - 1

        tmp = end - start + 1
        cnt += tmp

        p *= 10

    return cnt


def main():
    n = int(stdin.readline())
    ans = [0] * 10
    for k in range(10):
        ans[k] = count(n, k)
    stdout.write(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
