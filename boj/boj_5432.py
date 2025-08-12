from sys import stdin


def solve():
    T = int(stdin.readline().strip())
    for _ in range(T):
        n, k = map(int, stdin.readline().strip().split())
        
        loyal = [1] * n
        disloyal = [0] * n

        k -= n
        if k == 0:
            print(0, flush=False)
            continue

        for i in range((n + 2) // 3):
            disloyal[3*i] += 1
            k -= 1
            if k == 0:
                break

        while k > 0:
            disloyal[n-1] += 1
            k -= 1

            previous = loyal[n-2]
            loyal[n-2] = (disloyal[n-3] if n-3 >= 0 else 0) + (disloyal[n-2] if n-2 >= 0 else 0) + disloyal[n-1]
            k -= loyal[n-2] - previous

            previous = loyal[n-1]
            loyal[n-1] = (disloyal[n-2] if n-2 >= 0 else 0) + disloyal[n-1]
            k -= loyal[n-1] - previous

            if k < 0:
                disloyal[n-1] -= 1

        print(sum(disloyal), flush=False)


if __name__ == "__main__":
    solve()
