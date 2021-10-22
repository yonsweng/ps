from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    b = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a, b


def make_adj_list(x):
    adj = [[] for _ in range(len(x) + 1)]
    for i in range(len(x)):
        adj[x[i]].append(x[(i-1+len(x))%len(x)])
        adj[x[i]].append(x[(i+1)%len(x)])
    return adj


def find_route(adj_a, adj_b, start, n, started):
    route = []
    visited = set()

    now = start
    route.append(now)
    started[now] = True
    visited.add(now)

    a_side = [adj_a[now][0], adj_a[now][1]]
    b_side = [adj_b[now][0], adj_b[now][1]]

    for _ in range(n-1):
        go = False

        for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if a_side[i] == b_side[j]:
                now = a_side[i]
                route.append(now)
                started[now] = True
                visited.add(now)

                a_side[i] = adj_a[now][0] if adj_a[now][0] not in visited else adj_a[now][1]
                b_side[j] = adj_b[now][0] if adj_b[now][0] not in visited else adj_b[now][1]

                go = True
                break

        if not go:
            break

    return route if len(route) == n else None


def solve(n, a, b):
    adj_a = make_adj_list(a)
    adj_b = make_adj_list(b)

    answer = -1
    started = [False] * (n+1)

    for start in range(1, n+1):
        if not started[start]:
            route = find_route(adj_a, adj_b, start, n, started)  # list or None

            if route is not None:
                answer = ' '.join(map(str, route))
                break

    return answer


def main():
    input = read_input()
    answer = solve(*input)
    print(answer)


if __name__ == '__main__':
    main()
