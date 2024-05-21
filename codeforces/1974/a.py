from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        x, y = map(int, stdin.readline().split())
        area = x * 1 + y * 4
        a = (area + 14) // 15
        b = (y + 1) // 2 if y != 0 else 1
        answer = max(a, b) if x + y > 0 else 0
        print(answer, flush=False)


if __name__ == "__main__":
    main()
