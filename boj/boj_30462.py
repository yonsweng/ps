from sys import stdin


def solve():
    N = int(stdin.readline())
    B = list(map(int, stdin.readline().split()))
    A = [0] * N

    if B[-1] != N + 1:
        print("No")
        return

    no = False
    for i in range(N - 1):
        if B[i] > i + 2:
            no = True
            break
        if B[i] > B[i + 1]:
            no = True
            break
    if no:
        print("No")
        return

    print("Yes")
    candidates = set(range(1, N + 1))
    for i in range(N - 1):
        if B[i] != B[i + 1]:
            A[i + 1] = B[i]
            candidates.remove(B[i])
    for i in range(N):
        if A[i] == 0:
            A[i] = candidates.pop()
    print(*A)


if __name__ == "__main__":
    solve()
