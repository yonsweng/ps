from sys import stdin


def solve():
    T = int(stdin.readline())
    for t in range(T):
        N, L = map(int, stdin.readline().split())
        A = list(map(int, stdin.readline().split()))
        A.sort()
        cnt, last_time, total_time = 0, 0, 0
        for i in range(N):
            if last_time + A[i] > L:
                break
            cnt += 1
            last_time += A[i]
            total_time += last_time

        print(f"Case {t + 1}: {cnt} {last_time} {total_time}", flush=False)


if __name__ == "__main__":
    solve()
