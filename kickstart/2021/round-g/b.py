from sys import stdin
from itertools import product


def read_input():
    K = int(stdin.readline().rstrip())
    boxes = []
    for _ in range(K):
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        boxes.append((x1, y1, x2, y2))
    return K, boxes


def solve(K, boxes):
    min_sum_dist, ans_x, ans_y = 99999, 0, 0
    for x, y in product(range(-100, 101), range(-100, 101)):
        sum_dist = 0
        for x1, y1, x2, y2 in boxes:
            if x < x1:
                sum_dist += x1 - x
            elif x2 < x:
                sum_dist += x - x2

            if y < y1:
                sum_dist += y1 - y
            elif y2 < y:
                sum_dist += y - y2

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            ans_x, ans_y = x, y

    return f'{ans_x} {ans_y}'


def main():
    t = int(stdin.readline())

    for x in range(1, t + 1):
        input = read_input()
        answer = solve(*input)
        print(f'Case #{x}: {answer}')


if __name__ == '__main__':
    main()
