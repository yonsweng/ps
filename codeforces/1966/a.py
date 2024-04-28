from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = list(map(int, stdin.readline().split()))
        a = list(map(int, stdin.readline().split()))

        # find the number of the same numbers
        count = {}
        for i in a:
            if i not in count:
                count[i] = 0
            count[i] += 1

        flag = False
        for c in count.values():
            if c >= k:
                flag = True
                break

        if flag:
            print(k-1, flush=False)
        else:
            print(n, flush=False)


if __name__ == "__main__":
    main()