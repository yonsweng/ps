from collections import deque
from sys import stdin


def read_input():
    r, c = map(int, stdin.readline().split())  # read two integers of a line.
    g = [list(stdin.readline().strip()) for _ in range(r)]
    return r, c, g


def to_bits(alphabet):
    return 1 << (ord(alphabet) - ord("A"))


def is_valid(i, j, r, c):
    if i >= 0 and i < r and j >= 0 and j < c:
        return True
    return False


def solve(r, c, g):
    answer = 0

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    q = deque()
    inq = set()

    q0 = (0, 0, to_bits(g[0][0]), 1)
    q.append(q0)
    inq.add(q0)

    while len(q) > 0:
        qi = q.popleft()
        inq.remove(qi)
        i, j, check, cnt = qi

        answer = max(answer, cnt)

        for di, dj in directions:
            if (
                is_valid(i + di, j + dj, r, c)
                and (g_bits := to_bits(g[i + di][j + dj])) & check == 0
                and (qi := (i + di, j + dj, g_bits | check, cnt + 1))
                not in inq
            ):
                q.append(qi)
                inq.add(qi)

    return answer


def main():
    input = read_input()
    answer = solve(*input)
    print(answer)


if __name__ == "__main__":
    main()
