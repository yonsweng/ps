class SegTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(self.data))
        self.init(1, 0, len(self.data) - 1)

    def init(self, ti, l, r):
        if l == r:
            self.tree[ti] = self.data[l]
            return self.tree[ti]
        self.tree[ti] = self.init(ti * 2, l, (l + r) // 2) \
            + self.init(ti * 2 + 1, (l + r) // 2 + 1, r)
        return self.tree[ti]

    def __update__(self, ti, di, elt, l, r):
        if di < l or r < di:
            return self.tree[ti]
        if l == r:
            self.tree[ti] = elt
            return self.tree[ti]
        self.tree[ti] = self.__update__(ti * 2, di, elt, l, (l + r) // 2) \
            + self.__update__(ti * 2 + 1, di, elt, (l + r) // 2 + 1, r)
        return self.tree[ti]

    def __query__(self, ti, ql, qr, tl, tr):
        if ql <= tl and tr <= qr:
            return self.tree[ti]
        if tr < ql or qr < tl:
            return 0
        return self.__query__(ti * 2, ql, qr, tl, (tl + tr) // 2) \
            + self.__query__(ti * 2 + 1, ql, qr, (tl + tr) // 2 + 1, tr)

    def update(self, idx, elt):
        self.__update__(1, idx, elt, 0, len(self.data) - 1)

    def query(self, left, right):
        return self.__query__(1, left, right, 0, len(self.data) - 1)


def main():
    st = SegTree([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(st.query(4, 8))
    st.update(2, 1)
    st.update(5, 3)
    st.update(6, 10)
    print(st.query(2, 3))
    print(st.query(0, 6))


if __name__ == '__main__':
    main()
