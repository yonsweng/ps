from sys import stdin

input = stdin.readline
while True:
    n = input().strip()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes', flush=False)
    else:
        print('no', flush=False)