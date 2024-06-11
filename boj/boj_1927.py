from sys import stdin
from queue import PriorityQueue


def solve():
    n = int(stdin.readline())
    q = PriorityQueue(n)
    for _ in range(n):
        x = int(stdin.readline())
        if x == 0:
            if q.empty():
                print(0, flush=False)
            else:
                print(q.get(), flush=False)
        else:
            q.put(x)


if __name__ == "__main__":
    solve()
