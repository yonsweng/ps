from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def solve(n, a):
    answer = 0
    step = 0

    A = [a]

    while True:
        step += 1

        d = {}
        for ai in A[-1]:
            if ai in d:
                d[ai] += 1
            else:
                d[ai] = 1

        A.append([])

        changed = False
        for ai in A[-2]:
            A[-1].append(d[ai])
            if ai != d[ai]:
                changed = True

        if not changed:
            break

    q = int(stdin.readline())
    for _ in range(q):
        x, k = map(int, stdin.readline().split())
        if k >= len(A):
            print(A[-1][x-1])
        else:
            print(A[k][x-1])


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        solve(*input)


if __name__ == '__main__':
    main()
