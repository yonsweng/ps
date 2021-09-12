def i2r(i, m):
    return i // m


def i2c(i, m):
    return i % m


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = [(x, i) for i, x in enumerate(a)]
        b.sort()
        for i in range(0, n*m, m):
            b[i:i+m] = sorted(b[i:i+m], key=lambda x: x[0]*n*m-x[1])
        s = [0] * (n * m)
        for i in range(n * m):
            s[b[i][1]] = i
        r = [[] for _ in range(n)]
        answer = 0
        for i in range(n * m):
            row, col = i2r(s[i], m), i2c(s[i], m)
            for c in r[row]:
                if c < col:
                    answer += 1
            r[row].append(col)
        print(answer)


if __name__ == '__main__':
    main()
