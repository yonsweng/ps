from sys import stdin


def get_pi(S):
    pi = [0] * len(S)
    j = 0
    for i in range(1, len(S)):
        while j > 0 and S[i] != S[j]:
            j = pi[j - 1]
        if S[i] == S[j]:
            j += 1
            pi[i] = j
    return pi[-1]


def main():
    L = int(stdin.readline())
    S = stdin.readline().strip()
    print(L - get_pi(S))


if __name__ == "__main__":
    main()
