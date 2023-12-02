from sys import stdin


def main():
    f = [1, 1]
    while True:
        fi = f[-1] + f[-2]
        if fi > 10**16:
            break
        f.append(fi)

    # print(len(f))  # 78

    n = int(stdin.readline())
    for _ in range(n):
        k, x = map(int, stdin.readline().split())

        yes = False
        if k == 1:
            for fi in f:
                if fi > x:
                    break
                if fi == x:
                    yes = True
                    break
        elif k == 2:
            for i, fi in enumerate(f):
                for fj in f[i:]:
                    if fi + fj > x:
                        break
                    if fi + fj == x:
                        yes = True
                        break
                if yes:
                    break
        elif k == 3:
            for i, fi in enumerate(f):
                if fi > x:
                    break
                for j, fj in enumerate(f[i:]):
                    if fi + fj > x:
                        break
                    for fk in f[j:]:
                        if fi + fj + fk > x:
                            break
                        if fi + fj + fk == x:
                            yes = True
                            break
                    if yes:
                        break
                if yes:
                    break
        if yes:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
