from sys import stdin


def get_pi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(w, s):
    '''
    count how many times w is in s
    '''
    pi = get_pi(w)
    j = 0
    count = 0
    for i in range(len(s)):
        while j > 0 and s[i] != w[j]:
            j = pi[j - 1]
        if s[i] == w[j]:
            if j == len(w) - 1:
                count += 1
                j = pi[j]
            else:
                j += 1
    return count


def main():
    N = int(stdin.readline())
    for _ in range(N):
        A = stdin.readline().strip()
        W = stdin.readline().strip()
        S = stdin.readline().strip()

        next_ch = {}
        for i in range(len(A)):
            next_ch[A[i]] = A[(i + 1) % len(A)]

        shifts = []
        w = W
        for shift in range(len(A)):
            if kmp(w, S) == 1:
                shifts.append(shift)
            w = ''.join(map(lambda x: next_ch[x], w))

        if len(shifts) == 0:
            print("no solution", flush=False)
        elif len(shifts) == 1:
            print("unique:", shifts[0], flush=False)
        else:
            print("ambiguous:", ' '.join(map(str, shifts)), flush=False)


if __name__ == "__main__":
    main()
