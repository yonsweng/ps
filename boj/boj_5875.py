from sys import stdin


def solve():
    p = stdin.readline().strip()

    left_count = p.count("(")
    right_count = p.count(")")

    result = 0

    if left_count == right_count + 2:
        left_count, right_count = 0, 0
        for char in p[::-1]:
            if char == ")":
                right_count += 1
            else:
                left_count += 1
                if left_count > right_count:
                    result = left_count
                    break
    elif right_count == left_count + 2:
        left_count, right_count = 0, 0
        for char in p:
            if char == "(":
                left_count += 1
            else:
                right_count += 1
                if right_count > left_count:
                    result = right_count
                    break

    print(result)


if __name__ == "__main__":
    solve()
