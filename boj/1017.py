from sys import stdin
from math import sqrt


def is_prime(k):
    if k > 1:
        for i in range(2, int(sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True
    else:
        return False


def find_pair(i, graph, back, history):
    for j in graph[i]:
        if j not in history:
            history.add(j)
            if back[j] == -1 or find_pair(back[j], graph, back, history):
                back[j] = i
                return True
    return False


def main():
    n = int(stdin.readline())
    c = list(map(int, stdin.readline().split()))

    a, b = [], []
    first_remainder = c[0] % 2
    for ci in c:
        if ci % 2 == first_remainder:
            a.append(ci)
        else:
            b.append(ci)

    if len(a) != len(b):
        print(-1)
        return

    # adjacent list
    graph = [[] for _ in range(n // 2)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if is_prime(ai + bj):
                graph[i].append(j)

    answer = []
    for j in graph[0]:
        back = [-1] * (n // 2)
        back[j] = 0
        cnt = 1
        for i in range(1, n // 2):
            history = {j}
            cnt += int(find_pair(i, graph, back, history))
        if cnt == n // 2:
            answer.append(b[j])

    if len(answer) == 0:
        print(-1)
    else:
        print(" ".join(str(k) for k in sorted(answer)))


if __name__ == "__main__":
    main()
