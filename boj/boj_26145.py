from sys import stdin


def solve():
    N, M = map(int, stdin.readline().split())
    S = list(map(int, stdin.readline().split())) + [0] * M
    for i in range(N):
        Ti = list(map(int, stdin.readline().split()))
        for j, Tij in enumerate(Ti):
            S[i] -= Tij
            S[j] += Tij
    print(" ".join(map(str, S[: (N + M)])))


if __name__ == "__main__":
    solve()
