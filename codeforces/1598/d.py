from sys import stdin


def read_input():
    n = int(stdin.readline())
    a = [0]
    b = [0]
    for _ in range(n):
        ai, bi = map(int, stdin.readline().split())
        a.append(ai)
        b.append(bi)
    return n, a, b


def solve(n, a, b):
    topic = {}
    for i, ai in enumerate(a[1:], 1):
        if ai not in topic:
            topic[ai] = [i]
        else:
            topic[ai].append(i)

    diffi = {}
    for i, bi in enumerate(b[1:], 1):
        if bi not in diffi:
            diffi[bi] = [i]
        else:
            diffi[bi].append(i)

    answer = n * (n - 1) * (n - 2) // 6
    for t, problems in topic.items():
        if len(problems) >= 2:
            for problem in problems:
                answer -= len(diffi[b[problem]]) - 1

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
