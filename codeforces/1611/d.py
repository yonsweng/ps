from sys import stdin


def read_input():
    n = int(stdin.readline())
    b = [0] + list(map(int, stdin.readline().split()))
    p = [0] + list(map(int, stdin.readline().split()))
    return n, b, p


def solve(n, b, p):
    childs = [[] for _ in range(n+1)]
    root = 0
    for i, bi in enumerate(b[1:], 1):
        if i != bi:
            childs[bi].append(i)
        else:
            root = i

    allowed = {root}
    w = [0] * (n+1)
    dist = [0] * (n+1)
    max_dist = 0

    for pi in p[1:]:
        if pi in allowed:
            w[pi] = (max_dist + 1 - dist[b[pi]]) if pi != root else 0
            dist[pi] = dist[b[pi]] + w[pi]

            max_dist = max(max_dist, dist[pi])

            for child in childs[pi]:
                allowed.add(child)
            allowed.remove(pi)
        else:
            return -1

    return ' '.join(map(str, w[1:]))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
