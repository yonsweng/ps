from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    S = list(int(stdin.readline().strip()) for _ in range(N))

    S.sort()
    for i in range(1, N):
        if S[i] % 2 == 1 and S[i] != 1:
            S[0], S[i] = S[i], S[0]
            break

    latest = S[0]
    for i in range(1, N):
        if latest % 2 == 1:
            # Case 1
            latest += 2 + S[i]
        else:
            if S[i - 1] == 1:
                if S[i] == 1:
                    # Case 2
                    latest += 1
                else:
                    # Case 3
                    latest += 1 + 1 + (S[i] - 1)
            else:
                # Case 4
                latest += 2 + S[i]

    print((latest + 1) // 2)


if __name__ == "__main__":
    solve()
