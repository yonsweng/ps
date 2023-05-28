from sys import stdin


def solve():
    n_residents = [[0] * 15 for _ in range(15)]
    for room in range(1, 15):
        n_residents[0][room] = room
    for floor in range(1, 15):
        for room in range(1, 15):
            for i in range(1, room + 1):
                n_residents[floor][room] += n_residents[floor - 1][i]

    t = int(stdin.readline())
    for _ in range(t):
        k = int(stdin.readline())
        n = int(stdin.readline())
        print(n_residents[k][n], flush=False)


if __name__ == "__main__":
    solve()
