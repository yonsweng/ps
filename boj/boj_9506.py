from sys import stdin


def solve():
    while True:
        n = int(stdin.readline().strip())
        if n == -1:
            break

        divisors = []
        for d in range(1, n // 2 + 1):
            if n % d == 0:
                divisors.append(d)
        if sum(divisors) == n:
            print(f"{n} = " + " + ".join(map(str, divisors)))
        else:
            print(f"{n} is NOT perfect.")


if __name__ == "__main__":
    solve()
