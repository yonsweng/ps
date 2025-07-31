from sys import stdin

answer = set()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime_sums(H, total, i, count):
    if count == 0:
        if is_prime(total):
            answer.add(total)
    if i >= len(H):
        return
    find_prime_sums(H, total, i + 1, count)
    find_prime_sums(H, total + H[i], i + 1, count - 1)


def solve():
    N, M = map(int, stdin.readline().split())
    H = list(map(int, stdin.readline().split()))
    find_prime_sums(H, 0, 0, M)
    if len(answer) == 0:
        print(-1)
        return
    print(' '.join(map(str, sorted(answer))))


if __name__ == "__main__":
    solve()
