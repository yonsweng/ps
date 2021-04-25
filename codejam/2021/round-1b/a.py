# from time import time


# start_time = time()


def get_nanosec(X, Y, Z):
    for x in range(X, X + 43200000000000 * 1 + 1, 43200000000000):
        for y in range(Y, Y + 43200000000000 * 12 + 1, 43200000000000):
            for z in range(Z, Z + 43200000000000 * 12 * 60 + 1, 43200000000000):
                if (y - x) % 11 == 0 and (z - x) % 719 == 0 and (y - x) // 11 == (z - x) // 719:
                    return (y - x) // 11
    return -1


def print_hmsn(x, n):
    h = n // 3600000000000
    m = n // 60000000000 % 60
    s = n // 1000000000 % 60
    n = n % 1000000000
    print(f'Case #{x}: {h} {m} {s} {n}')


T = int(input())

for x in range(1, T + 1):
    A, B, C = map(int, input().split())

    n = get_nanosec(A, B, C)
    if n != -1:
        print_hmsn(x, n)
        continue

    n = get_nanosec(A, C, B)
    if n != -1:
        print_hmsn(x, n)
        continue

    n = get_nanosec(B, A, C)
    if n != -1:
        print_hmsn(x, n)
        continue

    n = get_nanosec(B, C, A)
    if n != -1:
        print_hmsn(x, n)
        continue

    n = get_nanosec(C, A, B)
    if n != -1:
        print_hmsn(x, n)
        continue

    n = get_nanosec(C, B, A)
    print_hmsn(x, n)


# print(time() - start_time)
