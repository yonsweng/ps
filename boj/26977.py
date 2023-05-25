from sys import stdin


def main():
    t = int(stdin.readline())

    for _ in range(t):
        stdin.readline()
        n, m = map(int, stdin.readline().split())

        b = []
        outputs = []

        for _ in range(m):
            bi, output = stdin.readline().split()
            b.append(bi)
            outputs.append(output)

        alive = set(range(m))

        while True:
            prev_n_alive = len(alive)

            for j in range(n):
                outputs_of_zero, outputs_of_one = set(), set()
                zero_indice, one_indice = [], []

                for i in range(m):
                    if i not in alive:
                        continue

                    if b[i][j] == "0":
                        outputs_of_zero.add(outputs[i])
                        zero_indice.append(i)
                    else:
                        outputs_of_one.add(outputs[i])
                        one_indice.append(i)

                if len(outputs_of_zero) == 1:
                    for index in zero_indice:
                        alive.remove(index)

                if len(outputs_of_one) == 1:
                    for index in one_indice:
                        alive.remove(index)

            if len(alive) == prev_n_alive:
                break

        if len(alive) <= 1:
            print("OK")
        else:
            print("LIE")


if __name__ == "__main__":
    main()
