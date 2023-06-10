from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        s = stdin.readline().rstrip()

        answer = ["." for _ in range(n)]
        gi, hi = 0, 0
        for i in range(k, n):
            if s[i - k] == "G" and i - k >= gi:
                answer[i] = "G"
                gi = i + k + 1
            elif s[i - k] == "H" and i - k >= hi:
                answer[i] = "H"
                hi = i + k + 1
        j = n - 1
        for i in range(n - k, n):
            if s[i] == "G" and i >= gi:
                while j > 0 and answer[j] != ".":
                    j -= 1
                if answer[j] == ".":
                    answer[j] = "G"
                gi = j + k + 1
            elif s[i] == "H" and i >= hi:
                while j > 0 and answer[j] != ".":
                    j -= 1
                if answer[j] == ".":
                    answer[j] = "H"
                hi = j + k + 1

        print(len(answer) - answer.count("."))
        print("".join(answer))


if __name__ == "__main__":
    solve()
