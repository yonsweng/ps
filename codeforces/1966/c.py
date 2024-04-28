from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        a = list(set(a))
        a.sort()

        prev = 0
        alice = True
        for i, ai in enumerate(a):
            if prev + 1 < ai or i == len(a) - 1:
                break
            prev = ai
            alice = not alice

        if alice:
            print("Alice", flush=False)
        else:
            print("Bob", flush=False)


if __name__ == "__main__":
    main()