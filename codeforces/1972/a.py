from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))

        answer = n
        for k in range(n):
            fail = False
            for i in range(n-k):
                j = i + k
                if a[i] > b[j]:
                    fail = True
                    break
            if not fail:
                answer = k
                break

        print(answer, flush=False)


if __name__ == "__main__":
    main()