from sys import stdin


def main():
    n = int(stdin.readline())
    c = list(map(int, stdin.readline().split()))
    c.sort(reverse=True)
    max_money, tuition = 0, 0
    for i, ci in enumerate(c):
        if (i + 1) * ci >= max_money:
            max_money = (i + 1) * ci
            tuition = ci
    print(max_money, tuition)


if __name__ == "__main__":
    main()
