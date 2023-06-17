from sys import stdin


def solve():
    a = list(map(int, stdin.readline().rstrip().split()))
    answer = 0
    p = 1
    for ai in a:
        answer += ai * p
        p *= 2
    print(answer)


if __name__ == "__main__":
    solve()
