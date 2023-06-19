from sys import stdin


def solve():
    q = int(stdin.readline())
    for _ in range(q):
        s = stdin.readline().rstrip()
        l = len(s)
        if "MOO" in s:
            print(l - 3)
        elif "MOM" in s or "OOO" in s:
            print(l - 2)
        elif "OOM" in s:
            print(l - 1)
        else:
            print(-1)


if __name__ == "__main__":
    solve()
