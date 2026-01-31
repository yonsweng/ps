from sys import stdin


def solve():
    p = stdin.readline().strip()

    if len(p) == 1:
        print(0)
        return

    if p[0] == ")" or p[-1] == "(":
        print(1)
        return

    left_count = p.count("(")
    right_count = p.count(")")

    if left_count == right_count:
        print(0)
        return

    result = 0

    if left_count == right_count + 2:
        left_count, right_count = 0, 0
        for char in p:
            if char == "(":
                left_count += 1
                if left_count > right_count + 1:
                    result += 1
            else:
                right_count += 1
    elif right_count == left_count + 2:
        left_count, right_count = 0, 0
        for char in p[::-1]:
            if char == "(":
                left_count += 1
            else:
                right_count += 1
                if right_count > left_count + 1:
                    result += 1

    print(result)


if __name__ == "__main__":
    solve()
