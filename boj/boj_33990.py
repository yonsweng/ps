from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    A, B, C = -1, -1, -1
    for _ in range(N):
        Ai, Bi, Ci = map(int, stdin.readline().strip().split())
        if Ai + Bi + Ci >= 512 and (A == -1 or Ai + Bi + Ci < A + B + C):
            A, B, C = Ai, Bi, Ci
    if A == -1:
        print(-1)
    else:
        print(A + B + C)


if __name__ == "__main__":
    solve()
