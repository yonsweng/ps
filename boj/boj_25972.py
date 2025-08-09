from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    dominos = []
    for _ in range(N):
        a, l = map(int, stdin.readline().strip().split())
        dominos.append((a, l))

    dominos.sort()

    answer = 1
    for i in range(1, N):
        if dominos[i][0] > dominos[i - 1][0] + dominos[i - 1][1]:
            answer += 1

    print(answer)


if __name__ == "__main__":
    solve()
