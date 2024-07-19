from sys import stdin
from queue import PriorityQueue


def main():
    N = int(stdin.readline())

    pq = PriorityQueue()
    for _ in range(N):
        x = int(stdin.readline())
        if x == 0:
            if pq.empty():
                print(0, flush=False)
            else:
                print(pq.get()[1], flush=False)
        else:
            pq.put((abs(x), x))


if __name__ == "__main__":
    main()
