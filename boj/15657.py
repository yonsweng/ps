from sys import stdout
from itertools import combinations_with_replacement

N, M = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

for t in combinations_with_replacement(s, M):
    stdout.write(' '.join(map(str, t)) + '\n')
