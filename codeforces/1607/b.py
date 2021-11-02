from sys import stdin


def read_input():
    x0, n = map(int, stdin.readline().split())
    return x0, n


def solve(x0, n):
    addition_odd = 0
    if n >= 1:
        addition_odd += 1
    addition_odd += max(0, n - 1) // 4 * 4
    if max(0, n - 1) % 4 == 1:
        addition_odd += -n
    elif max(0, n - 1) % 4 == 2:
        addition_odd += -(n - 1) - n
    elif max(0, n - 1) % 4 == 3:
        addition_odd += -(n - 2) - (n - 1) + n

    if x0 % 2 == 0:
        addition = -addition_odd
    else:
        addition = addition_odd

    answer = x0 + addition

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
