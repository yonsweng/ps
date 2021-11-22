from sys import stdin


def read_input():
    n = int(stdin.readline().rstrip())
    s = stdin.readline().rstrip()
    return n, s


def solve(n, s):
    indice = []

    left = 0
    right = n - 1

    while True:
        while left < n and s[left] != '1':
            left += 1
        while right >= 0 and s[right] != '0':
            right -= 1
        if left < right:
            indice.append(left + 1)
            indice.append(right + 1)
            left += 1
            right -= 1
        else:
            break

    indice.sort()

    if len(indice) == 0:
        return 0
    else:
        return '1\n' + str(len(indice)) + ' ' + ' '.join(map(str, indice))


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
