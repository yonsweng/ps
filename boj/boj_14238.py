from sys import stdin


def solve():
    s = stdin.readline().strip()

    a = s.count("A")
    b = s.count("B")
    c = s.count("C")

    n_cba = min(a, b, c)
    a -= n_cba
    b -= n_cba
    c -= n_cba

    result = []
    for _ in range(n_cba):
        if b > 0:
            result.append("B")
            b -= 1
        result.append("CBA")
    if b > 0:
        result.append("B")
        b -= 1

    n_caa = min(a // 2, c)
    for _ in range(n_caa):
        result.append("CAA")
        a -= 2
        c -= 1

    if a > 0:
        result.append("A")
        a -= 1
    if c == 1:
        result.append("C")
        c = 0
    if b > 0:
        for _ in range(b):
            if result[-1] == "B":
                print("-1")
                return
            result.append("B")
            if a > 0:
                result.append("A")
                a -= 1
        b = 0
    if a > 0:
        result.append("A" * a)
        a = 0

    if a > 0 or b > 0 or c > 0:
        print("-1")
        return

    print("".join(result))


if __name__ == "__main__":
    solve()
