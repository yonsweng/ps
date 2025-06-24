from sys import stdin


def solve():
    m = [0] * 10001
    m[3] = 4
    m[4] = 7
    for i in range(5, 10001):
        m[i] = m[i - 1] + m[i - 2]

    # Read input until EOF
    while True:
        line = stdin.readline().strip()
        if not line:
            break
        n = int(line)
        print(m[n], flush=False)


if __name__ == "__main__":
    solve()
