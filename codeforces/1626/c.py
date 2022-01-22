from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        k = list(map(int, stdin.readline().split()))
        h = list(map(int, stdin.readline().split()))

        for i in range(1, n):
            for j in range(i):
                diff_k = k[i] - k[j]
                if h[i] > diff_k:
                    h[i] = max(h[j] + diff_k, h[i])

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                diff_k = k[j] - k[i]
                if h[i] < h[j] - diff_k:
                    h[i] = h[j] - diff_k

        answer = 0
        for i in range(n - 1, -1, -1):
            m = min(k[i] - (k[i-1] if i-1 >= 0 else 0), h[i])
            answer += (2 * h[i] - m + 1) * m // 2

        print(answer)


if __name__ == '__main__':
    main()
