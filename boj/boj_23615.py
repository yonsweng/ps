from sys import stdin


def solve():
    _ = int(stdin.readline().strip())
    numbers = list(map(int, stdin.readline().strip().split()))

    zero_count = numbers.count(0)
    if zero_count >= 2:
        print("Yes\n0")
        return
    if zero_count == 1:
        print("No")
        return

    numbers.sort()
    min_number, max_number = numbers[0], numbers[-1]

    if max_number > 0:
        failed = False
        product = 1
        for number in numbers[:-1]:
            product *= number
            if abs(product) > max_number:
                failed = True
                break
        if product != max_number:
            failed = True

        if not failed:
            print("Yes")
            print(max_number)
            return

    if min_number < 0:
        failed = False
        product = 1
        for number in numbers[1:]:
            product *= number
            if abs(product) > -min_number:
                failed = True
                break
        if product != min_number:
            failed = True

        if not failed:
            print("Yes")
            print(min_number)
            return

    print("No")


if __name__ == "__main__":
    solve()
