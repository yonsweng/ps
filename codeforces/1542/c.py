import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

t = int(input())

for _ in range(t):
    n = int(input())

    answer = 0
    answer += 2 * (n // 2 + n % 2)
    answer += 3 * (n // 2)

    d = 2 * 3
    k = 4
    while d <= n:
        answer = (answer + n // d) % 1000000007

        d = lcm(d, k)
        k += 1

    print(answer)
