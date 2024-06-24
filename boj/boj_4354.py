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
    return pi


def main():
    while True:
        S = stdin.readline().strip()
        if S == ".":
            break

        pi = get_pi(S)

        if len(S) % (len(S) - pi[-1]) == 0:
            print(len(S) // (len(S) - pi[-1]), flush=False)
        else:
            print(1, flush=False)


if __name__ == "__main__":
    main()
