from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, m, k = map(int, stdin.readline().split())
        s = list(stdin.readline().strip())

        answer = 0
        zero_cnt = 0
        for i in range(n):
            if s[i] == "0":
                zero_cnt += 1
                if zero_cnt >= m:
                    answer += 1
                    for j in range(i, min(i + k, n)):
                        s[j] = "1"
                    zero_cnt = 0
            else:
                zero_cnt = 0

        print(answer, flush=False)


if __name__ == "__main__":
    solve()
