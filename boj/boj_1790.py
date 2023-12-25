def main():
    n, k = map(int, input().split())

    t = 1
    total = 0
    while True:
        total += 9 * t * 10 ** (t - 1)
        if total >= k:
            break
        t += 1

    m = 0
    for ti in range(t - 1):
        m += 9 * 10**ti

    total -= 9 * t * 10 ** (t - 1)
    x = m + (k - total - 1) // t + 1
    p = (k - total - 1) % t

    if n < x:
        print(-1)
    else:
        print(str(x)[p])


if __name__ == "__main__":
    main()
