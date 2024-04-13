from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(stdin.readline().strip().split())

        # count duplicate elements
        count = {}
        for i in a:
            count[i] = count.get(i, 0) + 1

        # sum counts
        total = 0
        for i in count:
            total += count[i] // 2

        print(total, flush=False)


if __name__ == '__main__':
    main()
