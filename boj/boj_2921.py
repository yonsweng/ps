from sys import stdin
from math import sqrt


def main():
    N, C = map(int, stdin.readline().split())
    L = [0] + list(map(int, stdin.readline().split()))
    M = int(stdin.readline())

    queries = []
    for i in range(M):
        a, b = map(int, stdin.readline().split())
        queries.append((a, b, i))

    queries.sort(key=lambda x: (N // sqrt(x[0]), x[1]))

    answer = [(False, 0)] * M
    cnt = [0] * (C + 1)
    left = right = 0

    for a, b, i in queries:
        while left < a:
            cnt[L[left]] -= 1
            left += 1

        while left > a:
            left -= 1
            cnt[L[left]] += 1

        while right < b:
            right += 1
            cnt[L[right]] += 1

        while right > b:
            cnt[L[right]] -= 1
            right -= 1

        max_cnt = max(cnt)
        if max_cnt > (b - a + 1) // 2:
            answer[i] = (True, cnt.index(max_cnt))
        else:
            answer[i] = (False, 0)

    for i, a in enumerate(answer):
        if a[0]:
            print(f"yes {a[1]}")
        else:
            print("no")


if __name__ == "__main__":
    main()


"""
10 3
1 2 1 2 1 2 3 2 3 3
8
1 2
1 3
1 4
1 5
2 5
2 6
6 9
7 10
"""
