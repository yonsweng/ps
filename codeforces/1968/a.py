from sys import stdin
from math import gcd


def main():
    t = int(stdin.readline())
    for _ in range(t):
        x = int(stdin.readline())
        max_value = 0
        y = 0
        for i in range(1, x):
            if i + gcd(i, x) > max_value:
                max_value = i + gcd(i, x)
                y = i
        print(y, flush=False)


if __name__ == "__main__":
    main()