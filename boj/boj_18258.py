from collections import deque
from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    q = deque()
    for _ in range(N):
        line = stdin.readline().strip()
        if line.startswith("push"):
            line = line.split()
            line[1] = int(line[1])
            q.append(line[1])
        elif line == "front":
            print(q[0] if q else -1, flush=False)
        elif line == "back":
            print(q[-1] if q else -1, flush=False)
        elif line == "pop":
            print(q.popleft() if q else -1, flush=False)
        elif line == "size":
            print(len(q), flush=False)
        elif line == "empty":
            print(1 if not q else 0, flush=False)


if __name__ == "__main__":
    solve()
