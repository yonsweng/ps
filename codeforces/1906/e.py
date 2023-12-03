from sys import stdin


def answer(n, c):
    groups = []
    stack = []
    max_c = max(c)
    for s in range(2 * n - 1, -1, -1):
        stack.append(c[s])
        if c[s] == max_c:
            group = []
            while stack:
                group.append(stack.pop())
            groups.append(group)
            if s > 0:
                max_c = max(c[:s])
    groups.reverse()
    cnts = [len(group) for group in groups]

    # split cnts into two groups with equal sum
    selected = set()
    dp = {}

    def dfs(i, remaining):
        if (i, remaining) in dp:
            return dp[(i, remaining)]
        if i == len(cnts):
            return remaining == 0
        if dfs(i + 1, remaining):
            dp[(i, remaining)] = True
            return True
        if remaining >= cnts[i] and dfs(i + 1, remaining - cnts[i]):
            selected.add(i)
            dp[(i, remaining)] = True
            return True
        dp[(i, remaining)] = False
        return False

    if not dfs(0, n):
        return [], []

    a, b = [], []
    for i in range(len(cnts)):
        if i in selected:
            a.extend(groups[i])
        else:
            b.extend(groups[i])

    return a, b


def main():
    n, c = int(stdin.readline().strip()), list(map(int, stdin.readline().split()))
    a, b = answer(n, c)
    if not a:
        print("-1")
    else:
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()
