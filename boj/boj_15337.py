from sys import stdin
from bisect import bisect_left


class SegmentTree:
    def __init__(self, n, op, e):
        self.n = n
        self.op = op
        self.e = e
        self.tree = [e] * (n * 4)

    def update(self, i, v):
        def _update(i, v, n, l, r):
            if i < l or r < i:
                return self.tree[n]
            if l == r:
                self.tree[n] = self.op(self.tree[n], v)
                return self.tree[n]
            m = (l + r) // 2
            self.tree[n] = self.op(
                _update(i, v, n * 2, l, m), _update(i, v, n * 2 + 1, m + 1, r)
            )
            return self.tree[n]

        return _update(i, v, 1, 0, self.n - 1)

    def query(self, l, r):
        def _query(l, r, n, nl, nr):
            if r < nl or nr < l:
                return self.e
            if l <= nl and nr <= r:
                return self.tree[n]
            m = (nl + nr) // 2
            return self.op(
                _query(l, r, n * 2, nl, m), _query(l, r, n * 2 + 1, m + 1, nr)
            )

        return _query(l, r, 1, 0, self.n - 1)


def policy1(p):
    p.sort(key=lambda x: x[1])

    op = lambda x, y: x + y
    e = 0
    st1 = SegmentTree(100000, op, e)
    st2 = SegmentTree(100000, op, e)

    overlaps = [0] * len(p)

    for i, (l, r) in enumerate(p):
        overlaps[i] += st1.query(l + 1, r)
        st1.update(r, 1)

    for j, (l, r) in enumerate(p[::-1]):
        i = len(p) - j - 1
        overlaps[i] += st2.query(l, r - 1)
        st2.update(l, 1)

    return max(overlaps) + 1


def policy2(p):
    a = []
    for l, r in p:
        a.append((l, 1))
        a.append((r, -1))

    a.sort()

    answer = 0
    count = 0
    for _, v in a:
        count += v
        answer = max(answer, count)

    return answer


def solve():
    n = int(stdin.readline())
    p = [list(map(int, stdin.readline().split())) for _ in range(n)]

    # coordinate compression
    x = sorted(set([x for x, _ in p] + [y for _, y in p]))
    for i in range(n):
        p[i][0] = bisect_left(x, p[i][0])
        p[i][1] = bisect_left(x, p[i][1])

    answer1 = policy1(p)
    answer2 = policy2(p)
    print(answer1, answer2)


if __name__ == "__main__":
    solve()
