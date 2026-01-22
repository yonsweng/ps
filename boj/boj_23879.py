from sys import stdin


def min_cmds(s):
    if len(s) == 1:
        return abs(s[0])

    result = 0

    if all(x > 0 for x in s):
        result += min(s)
        s = [x - min(s) for x in s]
    if all(x < 0 for x in s):
        result += -max(s)
        s = [x - max(s) for x in s]

    r = [s[0]]
    for si in s[1:]:
        if r[-1] * si <= 0:
            result += min_cmds(r)
            r = [si]
        else:
            r.append(si)
    result += min_cmds(r)

    return result


def solve():
    n = int(stdin.readline().strip())
    p = list(map(int, stdin.readline().strip().split()))
    t = list(map(int, stdin.readline().strip().split()))
    r = [p[i] - t[i] for i in range(n)]

    result = min_cmds(r)
    print(result)


if __name__ == "__main__":
    solve()
