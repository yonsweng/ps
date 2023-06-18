from sys import stdin

INF = 987654321


def backtrack(air_conditioners, remaining_temp, i, current_cost):
    if i == len(air_conditioners):
        for temp in remaining_temp:
            if temp > 0:
                return INF
        return current_cost

    a, b, p, m = air_conditioners[i]

    cost1 = backtrack(air_conditioners, remaining_temp, i + 1, current_cost)

    for j in range(a, b + 1):
        remaining_temp[j] -= p
    cost2 = backtrack(air_conditioners, remaining_temp, i + 1, current_cost + m)
    for j in range(a, b + 1):
        remaining_temp[j] += p

    return min(cost1, cost2)


def solve():
    n, m = map(int, stdin.readline().split())
    remaining_temp = [0] * 101
    for _ in range(n):
        s, t, c = map(int, stdin.readline().split())
        for i in range(s, t + 1):
            remaining_temp[i] = c

    air_conditioners = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

    print(backtrack(air_conditioners, remaining_temp, 0, 0))


if __name__ == "__main__":
    solve()
