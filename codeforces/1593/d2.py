from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    a = list(map(int, stdin.readline().rstrip().split()))
    return n, a


def dfs(i, cnt, m, n, a):
    for j in range(i + 1, n):
        if (a[j] - a[i]) % m == 0:
            cnt = dfs(j, cnt + 1, m, n, a)
            break

    return cnt


def solve(n, a):
    a.sort()

    cnts = {}
    for ai in a:
        if ai not in cnts:
            cnts[ai] = 1
        else:
            cnts[ai] += 1

    for cnt_value in cnts.values():
        if cnt_value >= n // 2:
            return -1

    for i, ai in enumerate(a):
        for j, aj in enumerate(a[i+1:n-n//2+2], i+1):
            if dfs(j, 2, aj-ai, n, a) >= n // 2:
                answer = max(answer, aj-ai)


    for m in range(max(a) - min(a), 0, -1):
        for i in range(n // 2 + 1):
            if dfs(i, 1, m, n, a) >= n // 2:
                return m

    return -1


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
