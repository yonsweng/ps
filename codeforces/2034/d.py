from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        moves = []

        ones = set()
        twos = []
        for i, ai in enumerate(a):
            if ai == 1:
                ones.add(i)
            elif ai == 2:
                twos.append(i)
        twos.reverse()

        left, right = 0, n - len(twos) - 1
        for i in range(n - 1, right, -1):
            if a[i] == 1:
                two_idx = twos.pop()
                ones.remove(i)
                ones.add(two_idx)
                moves.append((two_idx, i))
                a[i] = 2
                a[two_idx] = 1
            elif a[i] == 0:
                one_idx = next(iter(ones))
                two_idx = twos.pop()
                ones.remove(one_idx)
                ones.add(two_idx)
                moves.append((one_idx, i))
                moves.append((two_idx, i))
                a[i] = 2
                a[one_idx] = 0
                a[two_idx] = 1

        while left < right:
            if a[left] == 0:
                left += 1
                continue
            if a[right] == 1:
                right -= 1
                continue
            moves.append((left, right))
            a[left] = 0
            a[right] = 1
            left += 1
            right -= 1

        print(len(moves), flush=False)
        for u, v in moves:
            print(u + 1, v + 1, flush=False)


if __name__ == "__main__":
    solve()
