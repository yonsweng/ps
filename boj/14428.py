from sys import stdin


class SegTree:
    def __init__(self, data):
        self._data = data  # 0-indexed.
        self._tree = [(0, 0)] * (4 * len(self._data))
        self._init(1, 0, len(self._data) - 1)
        self._identity = (1000000001, 0)  # Please edit this.

    def _operation(self, a, b):
        return min(a, b)

    def _init(self, ti, dl, dr):
        if dl == dr:
            self._tree[ti] = (self._data[dl], dl)
            return self._tree[ti]
        self._tree[ti] = self._operation(
            self._init(ti * 2, dl, (dl + dr) // 2),
            self._init(ti * 2 + 1, (dl + dr) // 2 + 1, dr),
        )
        return self._tree[ti]

    def _update(self, ti, di, elt, dl, dr):
        if di < dl or dr < di:
            return self._tree[ti]
        if dl == dr:
            self._tree[ti] = (elt, dl)
            return self._tree[ti]
        self._tree[ti] = self._operation(
            self._update(ti * 2, di, elt, dl, (dl + dr) // 2),
            self._update(ti * 2 + 1, di, elt, (dl + dr) // 2 + 1, dr),
        )
        return self._tree[ti]

    def _query(self, ti, ql, qr, dl, dr):
        if ql <= dl and dr <= qr:
            return self._tree[ti]
        if dr < ql or qr < dl:
            return self._identity
        return self._operation(
            self._query(ti * 2, ql, qr, dl, (dl + dr) // 2),
            self._query(ti * 2 + 1, ql, qr, (dl + dr) // 2 + 1, dr),
        )

    def update(self, idx, elt):
        self._update(1, idx, elt, 0, len(self._data) - 1)

    def query(self, left, right):
        return self._query(1, left, right, 0, len(self._data) - 1)


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    st = SegTree(a)
    for _ in range(m):
        c, i, j = map(int, stdin.readline().split())
        if c == 1:
            st.update(i - 1, j)
        else:
            print(st.query(i - 1, j - 1)[1] + 1)


if __name__ == "__main__":
    main()
