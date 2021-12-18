from sys import stdin


def read_input():
    n, k, x = map(int, stdin.readline().split())
    s = stdin.readline().rstrip()
    return n, k, x, s


def solve(n, k, x, s):
    a = [len(si) * k for si in s.split('a') if si != '']

    na = [len(si) for si in s.split('*') if si != '']
    nb = []

    p = 1
    for i in range(len(a)-1, -1, -1):
        p *= a[i] + 1
        if x <= p:
            x -= 1
            while p > 1:
                p //= (a[i] + 1)
                nb.append(x // p)
                x %= p
                i += 1
            break

    answer = []
    if s[-1] == 'a':
        for nai, nbi in zip(na[::-1], nb[::-1]):
            answer.append(nai * 'a')
            answer.append(nbi * 'b')
        if len(na) > len(nb):
            for nai in na[len(na)-len(nb)-1::-1]:
                answer.append(nai * 'a')
    else:
        for nai, nbi in zip(na[::-1], nb[::-1]):
            answer.append(nbi * 'b')
            answer.append(nai * 'a')
        if len(na) < len(nb):
            answer.append(nb[0] * 'b')
        elif len(na) > len(nb):
            for nai in na[len(na)-len(nb)-1::-1]:
                answer.append(nai * 'a')

    answer = ''.join(answer[::-1])
    if answer == '':
        answer = 'b'

    return answer


def main():
    t = int(stdin.readline())
    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
