from sys import stdin

INF = 1000000000


def compute(F, children, me):
    if me not in children:
        return F[me], F[me]

    min_of_max, max_of_max, sum_of_total = INF, 0, 0
    for child in children[me]:
        maximum, total = compute(F, children, child)
        min_of_max = min(min_of_max, maximum)
        max_of_max = max(max_of_max, maximum)
        sum_of_total += total

    maximum = max(max_of_max, F[me])
    total = sum_of_total - min_of_max + max(min_of_max, F[me])
    return maximum, total


T = int(stdin.readline())

for x in range(1, T+1):
    N = int(stdin.readline())
    F = [0] + list(map(int, stdin.readline().split()))
    P = [0] + list(map(int, stdin.readline().split()))

    children = {}
    for i, Pi in enumerate(P[1:], 1):
        if Pi not in children:
            children[Pi] = []
        children[Pi].append(i)

    _, answer = compute(F, children, 0)
    print(f'Case #{x}: {answer}')
