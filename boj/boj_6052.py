from sys import stdin


def calc_pal(serial: int) -> int:
    """
    Calculate the sum of all divisors except the number itself of the given serial number.
    """
    total = 0
    for i in range(2, int(serial**0.5) + 1):
        if serial % i == 0:
            total += i
            if i != serial // i:
                total += serial // i
    total += 1  # 1 is always a divisor
    return total


def solve():
    S = int(stdin.readline().strip())

    serial = 1
    pals = set()
    while True:
        pal = calc_pal(serial)
        # print(serial, pal)
        if serial >= S and (pal, serial) in pals:
            if pal >= S:
                print(pal, serial)
            else:
                print(serial, pal)
            return
        pals.add((serial, pal))
        serial += 1


if __name__ == "__main__":
    solve()
