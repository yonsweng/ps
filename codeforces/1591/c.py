from sys import stdin


def read_input():
    n, k = map(int, stdin.readline().split())
    x = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, k, x


def solve(n, k, x):
    if n == 1:
        return abs(x[0])

    answer = 0

    x.sort()

    l, r = 0, n - 1

    if abs(x[0]) > abs(x[-1]) or x[-1] < 0:  # left is longer
        answer += abs(x[0])
        cnt = 0
        while cnt < k and x[l] <= 0:
            cnt += 1
            l += 1
    else:  # right is longer
        answer += abs(x[-1])
        cnt = 0
        while cnt < k and x[r] >= 0:
            cnt += 1
            r -= 1

    cnt = 0
    max_dist = 0
    while l <= r and x[l] < 0:
        max_dist = max(max_dist, abs(x[l]))
        cnt += 1
        if cnt == k:
            answer += max_dist * 2
            max_dist = 0
            cnt = 0
        l += 1
    
    if cnt > 0:
        answer += max_dist * 2
        max_dist = 0
        cnt = 0

    while l <= r and x[l] == 0:
        l += 1

    while l <= r:
        max_dist = max(max_dist, abs(x[r]))
        cnt += 1
        if cnt == k:
            answer += max_dist * 2
            max_dist = 0
            cnt = 0
        r -= 1

    if cnt > 0:
        answer += max_dist * 2
        max_dist = 0
        cnt = 0

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
