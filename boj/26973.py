from bisect import bisect_right
from sys import stdin
import math


def main():
    # eratosthenes sieve
    is_prime = [True] * 5000001
    for i in range(2, int(math.sqrt(5000000)) + 1):
        if is_prime[i]:
            for j in range(i * i, 5000001, i):
                is_prime[j] = False
    primes = [i for i in range(1, 5000001) if is_prime[i]]

    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        cnt = []
        for ai in a:
            if ai % 2 == 0:
                cnt.append(ai // 2)
            else:
                for i in range(bisect_right(primes, ai) - 1, -1, -1):
                    if (ai - primes[i]) % 4 == 0:
                        cnt.append(1 + (ai - primes[i]) // 2)
                        break

        min_cnt = min(cnt)
        if min_cnt % 2 == 1:
            print("Farmer John", flush=False)
        else:
            john = False
            for cnt_i in cnt:
                if cnt_i == min_cnt + 1:
                    john = True
                    break
                elif cnt_i == min_cnt:
                    break

            if john:
                print("Farmer John", flush=False)
            else:
                print("Farmer Nhoj", flush=False)


if __name__ == "__main__":
    main()
