from sys import stdout
from itertools import combinations

N, M = map(int, input().split())

for t in combinations(range(1, N + 1), M):
    stdout.write(' '.join(map(str, t)) + '\n')
