from sys import stdout
from itertools import permutations

N, M = map(int, input().split())
s = list(map(int, input().split()))
s.sort()

for t in permutations(s, M):
    stdout.write(' '.join(map(str, t)) + '\n')
