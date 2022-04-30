from sys import stdout
from itertools import combinations_with_replacement

N, M = map(int, input().split())

for t in combinations_with_replacement(range(1, N + 1), M):
    stdout.write(' '.join(map(str, t)) + '\n')
