from sys import stdin


def solve():
    n = int(stdin.readline())
    b = stdin.readline().rstrip()
    e = list(map(int, stdin.readline().split()))

    fgi = n
    for i in range(n):
        if b[i] == "G":
            fgi = i
            break
    lgi = -1
    for i in range(n - 1, -1, -1):
        if b[i] == "G":
            lgi = i
            break
    fhi = n
    for i in range(n):
        if b[i] == "H":
            fhi = i
            break
    lhi = -1
    for i in range(n - 1, -1, -1):
        if b[i] == "H":
            lhi = i
            break

    answer = 0
    if fgi < fhi and lhi <= e[fhi] - 1:
        if lgi <= e[0] - 1 or fhi <= e[0] - 1:
            answer += 1
        for i in range(1, fhi):
            if fhi <= e[i] - 1:
                answer += 1
    elif fhi < fgi and lgi <= e[fgi] - 1:
        if lhi <= e[0] - 1 or fgi <= e[0] - 1:
            answer += 1
        for i in range(1, fgi):
            if fgi <= e[i] - 1:
                answer += 1

    print(answer)


if __name__ == "__main__":
    solve()
