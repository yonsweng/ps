from sys import stdin


def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    answer = []
    i = 0
    direction = "R"
    sum_a = sum(a)
    while len(answer) < sum_a:
        answer.append(direction)
        a[i] -= 1

        if direction == "R":
            if i == n - 1 or (a[i] > 1 and a[i + 1] == 1) or a[i + 1] == 0:
                direction = "L"
                continue
            else:
                i += 1
        else:
            if i == 0 or (a[i] > 1 and a[i - 1] == 1) or a[i - 1] == 0:
                direction = "R"
                continue
            else:
                i -= 1

    print("".join(answer))


if __name__ == "__main__":
    solve()
