from sys import stdin


def hanoi(n, start, end):
    if n == 1:
        print(start, end, flush=False)
    else:
        hanoi(n - 1, start, 6 - start - end)
        print(start, end, flush=False)
        hanoi(n - 1, 6 - start - end, end)


n = int(stdin.readline())
print(2**n - 1, flush=False)
hanoi(n, 1, 3)
