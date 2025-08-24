from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    numerators, denominators = [], []
    for _ in range(n):
        v, c = map(int, stdin.readline().strip().split())
        numerators.append(v * c / 100)
        denominators.append(v)

    m = int(stdin.readline().strip())
    for _ in range(m):
        a, b, k = map(int, stdin.readline().strip().split())
        na = numerators[a - 1]
        numerators[a - 1] -= na * k / denominators[a - 1]
        numerators[b - 1] += na * k / denominators[a - 1]
        denominators[a - 1] -= k
        denominators[b - 1] += k

    print(n)
    for num, denom in zip(numerators, denominators):
        if denom == 0:
            print("0 0.0000")
        else:
            print(f"{denom} {num / denom * 100:.4f}")


if __name__ == "__main__":
    solve()
