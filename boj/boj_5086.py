from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print("factor", flush=False)
    elif a % b == 0:
        print("multiple", flush=False)
    else:
        print("neither", flush=False)
