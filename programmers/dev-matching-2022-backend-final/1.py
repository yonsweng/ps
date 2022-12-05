def vertical(img, i, j, size):
    for k in range(i, i + size):
        if img[k][j] == ".":
            return False
    return True


def calc_k(a, i, j, size):
    k = 0
    for ii in range(i + 1, i + size - 1):
        k += a[ii][j + size - 2] - a[ii][j]
    return k


def solution(low, high, img):
    answer = 0

    img = ["." * len(img[0])] + img + ["." * len(img[0])]
    for i in range(len(img)):
        img[i] = "." + img[i] + "."

    # print(img)

    a = [[0] * len(img[0]) for _ in range(len(img))]

    for i in range(len(img)):
        for j in range(len(img[i])):
            a[i][j] = a[i][j - 1] + (1 if img[i][j] == "#" else 0)

    # print(a)

    for size in range(3, min(len(img), len(img[0])) - 1):
        for i in range(1, len(img) - size + 1):
            for j in range(1, len(img[0]) - size + 1):
                # (i, j): top left
                # check if retangular
                print(i, j, size, calc_k(a, i, j, size))
                if (
                    a[i][j + size - 1] - a[i][j - 1] == size
                    and a[i + size - 1][j + size - 1] - a[i + size - 1][j - 1] == size
                    and vertical(img, i, j, size)
                    and vertical(img, i, j + size - 1, size)
                ):

                    # rectangular
                    if (
                        low * ((size - 2) ** 2)
                        <= calc_k(a, i, j, size) * 100
                        < high * ((size - 2) ** 2)
                    ):
                        print(i, j, size, calc_k(a, i, j, size))
                        answer += 1

    return answer


low = 25
high = 51
img = [
    ".########......",
    ".####...#......",
    ".#.####.#.#####",
    ".#.#..#.#.#..##",
    ".#.##.#.#.#...#",
    ".#.####.#.#...#",
    ".#....###.#####",
    ".########......",
]
print(solution(low, high, img))
