def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


m = int(input())
n = int(input())
primes = []
for k in range(m, n + 1):
    if is_prime(k):
        primes.append(k)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)
