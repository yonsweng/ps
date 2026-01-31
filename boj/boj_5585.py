from sys import stdin


def solve():
    money = int(stdin.readline().strip())
    money = 1000 - money

    count = 0
    for coin in [500, 100, 50, 10, 5, 1]:
        count += money // coin
        money %= coin
    print(count)


if __name__ == "__main__":
    solve()
