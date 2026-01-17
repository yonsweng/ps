from sys import stdin


def solve():
    T = int(stdin.readline())
    for _ in range(T):
        N = int(stdin.readline())
        P = list(map(int, stdin.readline().split()))

        output = []
        M = 0
        for i in range(N - 1):
            M = max(M, P[i])
            if M == i + 1:
                output.append(i + 1)
                P[i], P[i + 1] = P[i + 1], P[i]
                M = max(M, P[i])

        print(len(output), flush=False)
        print(*output, flush=False)


if __name__ == "__main__":
    solve()
