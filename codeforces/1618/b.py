from sys import stdin


def read_input():
    n = int(stdin.readline())
    b = list(stdin.readline().split())  # read several integers of a line.
    return n, b


def solve(n, b):
    answer = [b[0][0]]
    diff = False
    prev = b[0]
    for bi in b[1:]:
        if prev[-1] != bi[0]:
            diff = True
            answer.append(prev[-1])
        answer.append(bi[0])
        prev = bi
    answer.append(b[-1][-1])
    if not diff:
        answer.append(b[-1][-1])
    return ''.join(answer)


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
