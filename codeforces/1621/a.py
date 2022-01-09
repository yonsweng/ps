from sys import stdin


def read_input():
    n, k = map(int, stdin.readline().split())
    return n, k


def solve(n, k):
    rooks = []
    fail = False
    i, j = 0, 0
    for _ in range(k):
        if i < n and j < n:
            rooks.append((i, j))
        else:
            fail = True
            break
        i, j = i + 2, j + 2

    if not fail:
        answer = [['.'] * n for _ in range(n)]
        for rook in rooks:
            answer[rook[0]][rook[1]] = 'R'
        for i, row in enumerate(answer):
            answer[i] = ''.join(row)
        return '\n'.join(answer)
    else:
        return -1


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
