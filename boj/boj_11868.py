from sys import stdin


def main():
    _ = int(stdin.readline().rstrip())
    p = list(map(int, stdin.readline().rstrip().split()))

    xor = 0
    for pi in p:
        xor ^= pi

    print("koosaga" if xor else "cubelover")


if __name__ == "__main__":
    main()
