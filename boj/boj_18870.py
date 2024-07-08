from sys import stdin


def solve():
    stdin.readline()
    X = list(map(int, stdin.readline().split()))
    sorted_X = sorted(set(X))
    X_dict = {x: i for i, x in enumerate(sorted_X)}
    print(' '.join(str(X_dict[x]) for x in X))


if __name__ == '__main__':
    solve()
