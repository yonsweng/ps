from sys import stdin


class SegTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(self.data))
        self.lazy = [0] * (4 * len(self.data))
        self._init(1, 0, len(self.data) - 1)

    def _init(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = self.data[tl]
            return self.tree[i]
        self.tree[i] = self._init(i * 2, tl, (tl + tr) // 2) + self._init(
            i * 2 + 1, (tl + tr) // 2 + 1, tr
        )
        return self.tree[i]

    def _update(self, i, ql, qr, add, tl, tr):
        if qr < tl or tr < ql:  # [ql, qr] and [tl, tr] don't intersect.
            return
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            self.lazy[i] += add
            return
        self.lazy[i * 2] += self.lazy[i]
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.tree[i] += (self.lazy[i] + add) * (min(qr, tr) - max(ql, tl) + 1)
        self.lazy[i] = 0
        self._update(i * 2, ql, qr, add, tl, (tl + tr) // 2)
        self._update(i * 2 + 1, ql, qr, add, (tl + tr) // 2 + 1, tr)

    def _query(self, i, ql, qr, tl, tr):
        if qr < tl or tr < ql:  # [ql, qr] and [tl, tr] don't intersect.
            return 0
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            return self.tree[i] + self.lazy[i] * (tr - tl + 1)
        self.lazy[i * 2] += self.lazy[i]
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.tree[i] += self.lazy[i]
        self.lazy[i] = 0
        return self._query(i * 2, ql, qr, tl, (tl + tr) // 2) + self._query(
            i * 2 + 1, ql, qr, (tl + tr) // 2 + 1, tr
        )

    def update(self, left, right, add):
        self._update(1, left, right, add, 0, len(self.data) - 1)

    def query(self, left, right):
        return self._query(1, left, right, 0, len(self.data) - 1)


def main():
    _ = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())

    st = SegTree(a)
    for _ in range(m):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            st.update(query[1] - 1, query[2] - 1, query[3])
        else:
            print(st.query(query[1] - 1, query[1] - 1))


if __name__ == "__main__":
    main()
