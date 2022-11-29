from sys import stdin


class SegTree:
    def __init__(self, data):
        self._data = data  # 0-indexed.
        self._tree = [0] * (4 * len(self._data))
        self._init(1, 0, len(self._data) - 1)
        self._identity = 0

    def _operation(self, a, b):
        return a + b

    def _init(self, ti, dl, dr):
        if dl == dr:
            self._tree[ti] = self._data[dl]
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
            self._tree[ti] += elt
            return self._tree[ti]
        self._tree[ti] = self._operation(
            self._update(ti * 2, di, elt, dl, (dl + dr) // 2),
            self._update(ti * 2 + 1, di, elt, (dl + dr) // 2 + 1, dr),
        )
        return self._tree[ti]

    def _query(self, ti, dl, dr, accu, b):
        if dl == dr:  # leaf
            self.update(dl, -1)
            return dl
        if accu + self._tree[ti * 2] >= b:
            return self._query(ti * 2, dl, (dl + dr) // 2, accu, b)
        else:
            return self._query(
                ti * 2 + 1, (dl + dr) // 2 + 1, dr, accu + self._tree[ti * 2], b
            )

    def update(self, idx, elt):
        self._update(1, idx, elt, 0, len(self._data) - 1)

    def query(self, b):
        return self._query(1, 0, len(self._data) - 1, 0, b)


def main():
    st = SegTree([0] * 1000000)

    n = int(stdin.readline())
    for _ in range(n):
        splitted = stdin.readline().split()

        if len(splitted) == 2:
            _, b = map(int, splitted)
            print(st.query(b) + 1)
        else:
            _, b, c = map(int, splitted)
            st.update(b - 1, c)


if __name__ == "__main__":
    main()
