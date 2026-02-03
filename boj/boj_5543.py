from sys import stdin


def solve():
    hambergers = []
    for _ in range(3):
        hambergers.append(int(stdin.readline().strip()))
    drinks = []
    for _ in range(2):
        drinks.append(int(stdin.readline().strip()))
    total = min(hambergers) + min(drinks) - 50
    print(total)


if __name__ == "__main__":
    solve()
