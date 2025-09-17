from sys import stdin


def to_base(N, B):
    if N == 0:
        return "0"
    digits = []
    negative = N < 0
    N = abs(N)
    while N > 0:
        remainder = N % B
        if remainder >= 10:
            digits.append(chr(ord('A') + remainder - 10))
        else:
            digits.append(str(remainder))
        N //= B
    if negative:
        digits.append('-')
    return ''.join(reversed(digits))


def solve():
    N, B = stdin.readline().split()
    N = int(N)
    B = int(B)
    print(to_base(N, B))


if __name__ == "__main__":
    solve()
