from sys import stdin


def solve():
    while True:
        k, m = map(int, stdin.readline().strip().split())
        if k == 0 and m == 0:
            break

        satellites = []
        for _ in range(k):
            x, y, z = map(float, stdin.readline().strip().split())
            satellites.append((x, y, z))

        count = 0
        targets = []
        for j in range(m):
            x, y, z = map(float, stdin.readline().strip().split())
            targets.append((x, y, z))

            for i, (sx, sy, sz) in enumerate(satellites):
                ax, ay, az = -x, -y, -z
                bx, by, bz = sx - x, sy - y, sz - z
                cosine = (ax * bx + ay * by + az * bz) / (
                    ((ax**2 + ay**2 + az**2) ** 0.5) * ((bx**2 + by**2 + bz**2) ** 0.5)
                )
                # print(i, j, cosine)
                if cosine <= 0:
                    count += 1
                    break

        print(count)


if __name__ == "__main__":
    solve()
