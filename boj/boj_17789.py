from sys import stdin


def solve():
    p, v = map(int, stdin.readline().strip().split())

    pedestals = []
    for i in range(1, p + 1):
        a, b = map(int, stdin.readline().strip().split())
        if a > b:
            a, b = b, a
        pedestals.append((a, b, i))

    vases = []
    c = [0] + list(map(int, stdin.readline().strip().split()))
    for j in range(1, v + 1):
        vases.append((c[j], j))

    pedestals.sort()
    vases.sort()

    result = [0] * (v + 1)
    i, j = 0, 0
    while j < v:
        while i < p and pedestals[i][1] < vases[j][0]:
            i += 1
        if i < p:
            if pedestals[i][0] == vases[j][0]:
                result[vases[j][1]] = pedestals[i][2]
                i += 1
                j += 1
            elif pedestals[i][1] == vases[j][0]:
                result[vases[j][1]] = pedestals[i][2]
                i += 1
                j += 1
            else:
                i += 1
        else:
            print("impossible")
            return

    print("\n".join(map(str, result[1:])))


if __name__ == "__main__":
    solve()
