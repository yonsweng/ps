def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = [(x, i) for i, x in enumerate(a)]
        b.sort(key=lambda x: n*m*x[0]-x[1])
        s = [0] * m
        for i in range(m):
            s[b[i][1]] = i
        answer = 0
        for i in range(m):
            for j in range(i):
                if s[j] < s[i]:
                    answer += 1
        print(answer)


if __name__ == '__main__':
    main()
