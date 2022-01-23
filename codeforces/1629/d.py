from sys import stdin
from string import ascii_lowercase


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        s = [stdin.readline().rstrip() for _ in range(n)]

        yes = False

        for si in s:
            if si[0] == si[-1]:
                yes = True
                break

        if yes:
            print('YES')
            continue

        candidates = set()
        for si in s:
            if si in candidates:
                yes = True
                break

            candidates.add(si[::-1])
            candidates.add(si[:2][::-1])
            if len(si) == 2:
                for c in ascii_lowercase:
                    candidates.add((si + c)[::-1])

        if yes:
            print('YES')
            continue

        print('NO')


if __name__ == '__main__':
    main()
