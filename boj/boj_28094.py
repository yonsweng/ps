from itertools import permutations
from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        adj = [[0] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            v, a, b = map(int, stdin.readline().split())
            adj[a][b] += v
        highest_score, n_arrangements = 0, 0
        for perm in permutations(range(1, n + 1)):
            score = 0
            for i in range(n - 1):
                for j in range(i + 1, n):
                    score += adj[perm[i]][perm[j]]
            if score > highest_score:
                highest_score = score
                n_arrangements = 1
            elif score == highest_score:
                n_arrangements += 1
        print(highest_score, n_arrangements)


if __name__ == "__main__":
    solve()
