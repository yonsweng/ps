from sys import stdin


def main():
    zeros = [[] for _ in range(200001)]
    p = 1
    for _ in range(18):
        cnt = 0
        zeros[0].append(0)
        for i in range(1, 200001):
            if i & p == 0:
                cnt += 1
            zeros[i].append(cnt)
        p <<= 1

    t = int(stdin.readline())
    for _ in range(t):
        l, r = map(int, stdin.readline().split())
        answer = min([zeros[r][i] - zeros[l-1][i] for i in range(18)])
        print(answer)


if __name__ == '__main__':
    main()
