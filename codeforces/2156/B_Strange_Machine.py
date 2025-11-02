from sys import stdin


def solve():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, q = map(int, stdin.readline().strip().split())
        s = stdin.readline().strip()
        a = list(map(int, stdin.readline().strip().split()))

        if all(c == "A" for c in s):
            for ai in a:
                print(ai, flush=False)
            continue

        for ai in a:
            steps = 0
            while ai > 0:
                if s[steps % n] == "A":
                    ai -= 1
                elif s[steps % n] == "B":
                    ai //= 2
                steps += 1
            print(steps, flush=False)


if __name__ == "__main__":
    solve()
