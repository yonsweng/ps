from sys import stdin


def read_input():
    n, k = map(int, stdin.readline().rstrip().split())
    x = list(map(int, stdin.readline().rstrip().split()))
    return n, k, x


def solve(n, k, x):
    x.sort()
    accu = 0
    cnt = 0
    cat = 0
    for xi in x[::-1]:
        if xi <= cat:
            break
        accu += n - xi
        cat += n - xi
        if accu > n:
            break
        cnt += 1
    return cnt


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
