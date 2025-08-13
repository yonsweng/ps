from sys import stdin


def solve():
    while True:
        H, W, S, L = map(int, stdin.readline().split())
        if H == 0 and W == 0 and S == 0 and L == 0:
            break
        
        image = [[(-1, -1, -1)] * (W + 2)]
        for _ in range(H):
            row = list(map(int, stdin.readline().split()))
            row = [(-1, -1, -1)] + [
                (row[j] // S, row[j+1] // S, row[j+2] // S) for j in range(0, len(row), 3)
            ] + [(-1, -1, -1)]
            image.append(row)
        image.append([(-1, -1, -1)] * (W + 2))

        area = [[0] * (W + 2) for _ in range(H + 2)]
        color_count = 0
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                if image[i][j] == (-1, -1, -1):
                    continue
                if area[i][j] != 0:
                    continue
                color_count += 1
                area_size = 1
                color = image[i][j]
                stack = [(i, j)]
                area[i][j] = color_count
                while stack:
                    x, y = stack.pop()
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if image[nx][ny] != color or area[nx][ny] != 0:
                                continue
                            area[nx][ny] = color_count
                            stack.append((nx, ny))
                            area_size += 1

                if area_size < L:
                    color_count -= 1

        print(color_count)


if __name__ == "__main__":
    solve()
