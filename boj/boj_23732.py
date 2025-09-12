from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    S = stdin.readline().strip()

    answer = N * (N + 1) // 2
    prev = -1
    for i in range(N - 1):
        if S[i] == S[i+1]:
            k = i - prev
            answer -= k * (k + 1) // 2
            prev = i
    k = N - 1 - prev
    answer -= k * (k + 1) // 2

    print(answer)


if __name__ == "__main__":
    solve()
