from sys import stdin


def solve():
    n = int(stdin.readline())
    for _ in range(n):
        p, k, l = map(int, stdin.readline().split())
        f = list(map(int, stdin.readline().split()))
        f.sort(reverse=True)
        answer = 0
        t = 1
        cnt = 0
        for i in range(l):
            answer += f[i] * t
            cnt += 1
            if cnt == k:
                cnt = 0
                t += 1

        print("Case #{}: {}".format(_ + 1, answer))


if __name__ == "__main__":
    solve()
