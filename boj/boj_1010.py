from sys import stdin
from math import comb


def main():
    T = int(stdin.readline())
    for _ in range(T):
        N, M = map(int, stdin.readline().split())
        print(comb(M, N))


if __name__ == "__main__":
    main()
