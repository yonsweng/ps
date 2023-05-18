from sys import stdin


def main():
    n = int(stdin.readline())
    r = [[]]
    for i in range(1, n + 1):
        r.append([0] * i + list(map(int, stdin.readline().split())))

    b = [0, 0]
    for i in range(2, n + 1):
        for candidate in (b[i - 1] + r[i - 1][i], b[i - 1] - r[i - 1][i]):
            good = True
            minimum, maximum = min(b[i - 1], candidate), max(b[i - 1], candidate)
            for j in range(i - 2, 0, -1):
                minimum, maximum = min(minimum, b[j]), max(maximum, b[j])
                if maximum - minimum != r[j][i]:
                    good = False
                    break
            if good:
                b.append(candidate)
                break

    print(" ".join(map(str, b[1:])))


if __name__ == "__main__":
    main()
