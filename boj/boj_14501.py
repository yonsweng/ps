def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    d = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if i + a[i][0] > n:
            d[i] = d[i + 1]
        else:
            d[i] = max(d[i + 1], d[i + a[i][0]] + a[i][1])
    print(d[0])


if __name__ == "__main__":
    main()
