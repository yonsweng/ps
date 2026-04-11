from collections import deque
from sys import stdin


def solve():
    n, k = map(int, stdin.readline().split())
    children = [[] for _ in range(n)]
    for _ in range(n - 1):
        p, c = map(int, stdin.readline().split())
        children[p].append(c)
    apple = list(map(int, stdin.readline().split()))

    q = deque([(0, 0)])
    answer = 0
    while q:
        node, dist = q.popleft()
        if dist > k:
            break
        answer += apple[node]
        for child in children[node]:
            q.append((child, dist + 1))

    print(answer)


if __name__ == "__main__":
    solve()
