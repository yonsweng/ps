from sys import stdin


def read_input():
    b = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return b,


def solve(b):
    x = b[0]
    y = b[1]
    z = b[-1] - x - y
    answer = f'{x} {y} {z}'
    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
