def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = [0] * (2 * n)
        bb = [(j, B) for j, B in enumerate(b)]
        bb = sorted(bb, key=lambda x: x[1])
        m = 99999999
        for i in range(n-1, -1, -1):
            j, B = bb[i]
            m = min(m, j)
            c[B-1] = m
        answer = 99999999
        for i in range(n):
            answer = min(answer, c[a[i]] + i)
        print(answer)


if __name__ == '__main__':
    main()
