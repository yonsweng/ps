from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

INF = 999
N_COLORS = 20


def get_input():
    input = stdin.readline
    n, k = map(int, input().split())
    lights = list(map(int, input().split()))
    return n, k, lights


def min_count(i, j, lights, dp):
    if dp[i][j] != INF:
        return dp[i][j]

    if i == j:
        return 0
    
    if i + 1 == j:
        return 1 if lights[i] != lights[j] else 0

    ret = INF
    for k in range(i, j):
        left = min_count(i, k, lights, dp)
        right = min_count(k + 1, j, lights, dp)
        ret = min(ret, left + right + (0 if lights[i] == lights[j] else 1))

    dp[i][j] = ret
    return dp[i][j]


def solution(n, k, lights):
    dp = [[INF] * n for _ in range(n)]
    return min_count(0, n - 1, lights, dp)


if __name__ == "__main__":
    n, k, lights = get_input()
    print(solution(n, k, lights))
