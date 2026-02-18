from sys import stdin


def solve():
    n, k = map(int, stdin.readline().split())
    countries = []
    j = 0
    for _ in range(n):
        i, gold, silver, bronze = map(int, stdin.readline().split())
        countries.append((i, gold, silver, bronze))
        if i == k:
            j = len(countries) - 1

    rank = 1
    for i, gold, silver, bronze in countries:
        if (
            gold > countries[j][1]
            or (gold == countries[j][1] and silver > countries[j][2])
            or (
                gold == countries[j][1]
                and silver == countries[j][2]
                and bronze > countries[j][3]
            )
        ):
            rank += 1

    print(rank)


if __name__ == "__main__":
    solve()
