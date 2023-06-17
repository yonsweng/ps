from sys import stdin


def solve():
    n = int(stdin.readline().rstrip())
    s = stdin.readline().rstrip()
    r = []
    for si in s:
        r.append(si)
        r.append(si)
    print("".join(r))


if __name__ == "__main__":
    solve()
