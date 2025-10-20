from sys import stdin


def solve():
    S, C = stdin.readline().strip().split()

    for i in range(300):
        if S == C:
            print(i)
            return

        new_S = ""
        prev_char = S[0]
        count = 1
        for j in range(1, len(S)):
            if S[j] == prev_char:
                count += 1
            else:
                new_S += str(count) + prev_char
                prev_char = S[j]
                count = 1
        new_S += str(count) + prev_char
        S = new_S


if __name__ == "__main__":
    solve()
