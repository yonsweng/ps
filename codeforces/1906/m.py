from sys import stdin


def max_n_of_non_degenerate_triangles(n, a):
    max_a = max(a)
    sum_others = sum(a) - max_a
    if sum_others < max_a // 2:
        return sum_others
    return (max_a + sum_others) // 3


def main():
    n, a = int(stdin.readline().strip()), list(map(int, stdin.readline().split()))
    print(max_n_of_non_degenerate_triangles(n, a))


if __name__ == "__main__":
    main()
