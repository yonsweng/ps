import sys
from sys import stdin


def main():
    n = int(stdin.readline())

    low, high = 1, n - 1
    m = n
    accu = 0
    prev_answer = 0
    while low < high:
        mid = (low + high) // 2
        print(f'+ {m - mid}')
        accu += m - mid
        sys.stdout.flush()
        answer = int(stdin.readline())
        if answer == prev_answer:
            low = low + (m - mid)
            high = m - 1
        else:
            low = m
            high = high + (m - mid)
            m += n

        prev_answer = answer

    print(f'! {low}')


if __name__ == '__main__':
    main()
