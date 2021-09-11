import math


def is_prime(t):
    if t == 1:
        return False
    for i in range(2, int(math.sqrt(t)) + 1):
        if t % i == 0:
            return False
    return True


def solution(N, k):
    answer = 0

    n = N
    m = []
    while n > 0:
        m.append(str(n % k))
        n //= k
    m = ''.join(reversed(m))
    # print(m)

    m = m.split('0')

    for t in m:
        if t == '':
            continue

        t = int(t)
        if is_prime(t):
            answer += 1
        # print(t, answer)

    return answer


n = 110011
k = 10

result = solution(n, k)
print(result)
