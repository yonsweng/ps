from sys import stdin


def divide(n):
    for divisor in range(9, 1, -1):
        if n % divisor == 0:
            return n // divisor, divisor
    return n, 1


def solve():
    while True:
        n = int(stdin.readline().strip())
        if n == -1:
            break

        if len(str(n)) == 1:
            print(f"1{n}")
            continue

        no_such_number = False
        reversed_answer = []
        while n > 1:
            n, divisor = divide(n)
            if divisor == 1:
                no_such_number = True
                break
            reversed_answer.append(str(divisor))

        if no_such_number:
            print("There is no such number.")
        else:
            print("".join(reversed(reversed_answer)))


if __name__ == "__main__":
    solve()
