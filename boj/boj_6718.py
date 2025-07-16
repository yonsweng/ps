from sys import stdin


def calc_is_prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    primes = []

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return is_prime, primes


def solve():
    is_prime, primes = calc_is_prime(2 ** 15)

    while True:
        n = int(stdin.readline().strip())
        if n == 0:
            break

        cnt = 0
        for prime in primes:
            if prime > n // 2:
                break
            if is_prime[n - prime]:
                cnt += 1

        print(cnt, flush=False)


if __name__ == "__main__":
    solve()
