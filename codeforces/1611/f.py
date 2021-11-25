from sys import stdin


def read_input():
    n, s = map(int, stdin.readline().split())
    a = [0] + list(map(int, stdin.readline().split()))
    return n, s, a


def solve(n, s, a):
    max_len = 0
    answer_left, answer_right = -1, -1
    left, right = 1, 1
    accu = 0
    while right <= n:
        accu += a[right]

        if s + accu < 0:
            while s + accu < 0:
                accu -= a[left]
                left += 1

            right += 1

            if right < left:
                right = left
        else:
            right += 1

            if max_len < right - left:
                max_len = right - left
                answer_left = left
                answer_right = right - 1

    if answer_left != -1:
        return f'{answer_left} {answer_right}'
    else:
        return -1


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
