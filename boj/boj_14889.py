from sys import stdin

ans = 900


def dfs(s, visited, group1, group2, n, idx):
    global ans

    if idx == n:
        sum1, sum2 = 0, 0
        for i in range(len(group1)):
            for j in range(i + 1, len(group1)):
                sum1 += s[group1[i]][group1[j]] + s[group1[j]][group1[i]]
                sum2 += s[group2[i]][group2[j]] + s[group2[j]][group2[i]]
        ans = min(ans, abs(sum1 - sum2))
        return
    
    if len(group1) < n // 2:
        group1.append(idx)
        dfs(s, visited, group1, group2, n, idx + 1)
        group1.pop()

    if len(group2) < n // 2:
        group2.append(idx)
        dfs(s, visited, group1, group2, n, idx + 1)
        group2.pop()


def main():
    n = int(stdin.readline())
    s = [list(map(int, stdin.readline().split())) for _ in range(n)]

    visited = [False] * n
    group1, group2 = [0], []

    dfs(s, visited, group1, group2, n, 1)
    print(ans)


if __name__ == "__main__":
    main()
