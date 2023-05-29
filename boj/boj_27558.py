from sys import stdin


def solve():
    t = int(stdin.readline())
    for _ in range(t):
        a = stdin.readline().rstrip()
        b = stdin.readline().rstrip()

        if a == b:
            print(0, flush=False)
            continue

        n = len(a)
        c = {}
        impossible = False
        for i in range(n):
            if a[i] not in c:
                c[a[i]] = b[i]
            else:
                if c[a[i]] != b[i]:
                    impossible = True
                    break
        if impossible:
            print(-1, flush=False)
            continue

        # find cycles
        cycles = {}
        visited = set()
        for ai, bi in c.items():
            if ai in visited or ai == bi:
                continue
            visited.add(ai)
            cycle = {ai}
            while bi in c:
                if bi in visited:
                    if bi == ai:
                        for ci in cycle:
                            cycles[ci] = c[ci]
                    else:
                        while bi in c and bi not in cycle:
                            cycle.add(bi)
                            cycles.pop(bi, None)
                            bi = c[bi]
                    break
                visited.add(bi)
                cycle.add(bi)
                bi = c[bi]

        # count cycles
        cycle_count = 0
        visited = set()
        for ai, bi in cycles.items():
            if ai in visited:
                continue
            visited.add(ai)
            cycle_count += 1
            while bi in cycles:
                if bi in visited:
                    break
                visited.add(bi)
                bi = cycles[bi]

        cnt = 0
        bs = set()
        for ai, bi in c.items():
            bs.add(bi)
            if ai != bi:
                cnt += 1

        # if cnt == 52 and cycle_count > 0:
        #     print(-1, flush=False)
        #     continue

        if len(bs) == 52:
            print(-1, flush=False)
            continue

        answer = cnt + cycle_count
        print(answer, flush=False)


if __name__ == "__main__":
    solve()
