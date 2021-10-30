from sys import stdin
from collections import deque


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = [0] + list(map(int, stdin.readline().split()))  # read several integers of a line.
    b = [0] + list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a, b


def solve(n, a, b):
    min_jumps = [999999] * (n + 1)
    trace = [(-1, -1)] * (n + 1)

    min_jumps[n] = 0

    q = deque()
    in_q = set()
    q.append((n, 0))  # (depth, jumps)
    in_q.add((n, 0))

    finished = False

    while len(q) != 0:
        depth, jumps = q.popleft()
        in_q.remove((depth, jumps))

        for dest in range(depth, max(0, depth-a[depth]) - 1, -1):
            before = dest
            dest = dest + b[dest]

            if dest == 0:
                finished = True
                min_jumps[dest] = jumps + 1
                trace[dest] = (depth, before)
                break

            if min_jumps[dest] > jumps + 1:
                min_jumps[dest] = jumps + 1
                trace[dest] = (depth, before)

                if (dest, jumps + 1) not in in_q:
                    q.append((dest, jumps + 1))
                    in_q.add((dest, jumps + 1))

        if finished:
            break

    if min_jumps[0] == 999999:
        return -1

    # print(trace)

    T = deque()
    t = trace[0]
    while t != (-1, -1):
        T.appendleft(t[1])
        t = trace[t[0]]

    answer = str(min_jumps[0]) + '\n' + ' '.join(map(str, T))
    return answer


def main():
    for _ in range(1):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
