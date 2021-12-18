from sys import stdin


def main():
    q = int(stdin.readline())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, stdin.readline().split())))
    answer = []
    replace = {}
    for query in reversed(queries):
        if query[0] == 1:
            answer.append(replace.get(query[1], query[1]))
        else:
            replace[query[1]] = replace.get(query[2], query[2])
    print(' '.join(map(str, reversed(answer))))


if __name__ == '__main__':
    main()
