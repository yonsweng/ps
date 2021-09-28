from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    return n, a


def argmin(a, l, n):
    min_val, arg_min = 1000000000, l
    for i in range(l, n + 1):
        if a[i] < min_val:
            min_val = a[i]
            arg_min = i
    return arg_min


def rotate(a, l, r, d):
    a[l:r+1] = a[l+d:r+1] + a[l:l+d]


def solve(n, a):
    answer = []  # [(l, r, d), ...]

    for l in range(1, n):
        r = argmin(a, l, n)

        if r == l:
            continue

        length = r - l + 1
        d = length - 1
        answer.append((l, r, d))

        rotate(a, l, r, d)

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        n, a = read_input()
        answer = solve(n, a)

        print(len(answer))
        for l, r, d in answer:
            print(l, r, d)


if __name__ == '__main__':
    main()
