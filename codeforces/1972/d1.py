from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())

        answer = 0
        for b in range(1, m+1):
            answer += (n // b + 1) // b
        answer -= 1

        print(answer, flush=False)


if __name__ == "__main__":
    main()
