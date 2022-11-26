from sys import stdin, setrecursionlimit


def read_input():
    n = int(stdin.readline())  # read an integer.
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(
            int, stdin.readline().split()
        )  # read two integers of a line.
        g[u].append(v)
        g[v].append(u)
    return n, g


def min_adapters(g, dp, i, j, parent):
    if dp[i][j] != -1:
        return dp[i][j]

    ret = 0
    if j == 0:
        for k in g[i]:
            if k != parent:
                ret += min_adapters(g, dp, k, 1, i)
    else:
        ret += 1
        for k in g[i]:
            if k != parent:
                ret += min(
                    min_adapters(g, dp, k, 0, i),
                    min_adapters(g, dp, k, 1, i),
                )
    dp[i][j] = ret
    return ret


def solve(n, g):
    answer = 0

    dp = [[-1, -1] for _ in range(n + 1)]
    answer += min(min_adapters(g, dp, 1, 0, -1), min_adapters(g, dp, 1, 1, -1))

    return answer


def main():
    setrecursionlimit(1100000)
    input = read_input()
    answer = solve(*input)
    print(answer)


if __name__ == "__main__":
    main()
