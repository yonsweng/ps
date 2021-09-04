class SegTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (4 * len(self.data))
        self.lazy = [0] * (4 * len(self.data))
        self.init(1, 0, len(self.data) - 1)

    def init(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = self.data[tl]
            return self.tree[i]
        self.tree[i] = self.init(i * 2, tl, (tl + tr) // 2) \
            + self.init(i * 2 + 1, (tl + tr) // 2 + 1, tr)
        return self.tree[i]

    def __update__(self, i, ql, qr, add, tl, tr):
        if qr < tl or tr < ql:  # [ql, qr] and [tl, tr] don't intersect.
            return
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            self.lazy[i] += add
            return
        self.lazy[i*2] += self.lazy[i]
        self.lazy[i*2+1] += self.lazy[i]
        self.tree[i] += (self.lazy[i] + add) * (min(qr, tr) - max(ql, tl) + 1)
        self.lazy[i] = 0
        self.__update__(i * 2, ql, qr, add, tl, (tl + tr) // 2)
        self.__update__(i * 2 + 1, ql, qr, add, (tl + tr) // 2 + 1, tr)

    def __query__(self, i, ql, qr, tl, tr):
        if qr < tl or tr < ql:  # [ql, qr] and [tl, tr] don't intersect.
            return 0
        if ql <= tl and tr <= qr:  # [ql, qr] includes [tl, tr].
            return self.tree[i] + self.lazy[i] * (tr - tl + 1)
        self.lazy[i*2] += self.lazy[i]
        self.lazy[i*2+1] += self.lazy[i]
        self.tree[i] += self.lazy[i]
        self.lazy[i] = 0
        return self.__query__(i * 2, ql, qr, tl, (tl + tr) // 2) \
            + self.__query__(i * 2 + 1, ql, qr, (tl + tr) // 2 + 1, tr)

    def update(self, left, right, add):
        self.__update__(1, left, right, add, 0, len(self.data) - 1)

    def query(self, left, right):
        return self.__query__(1, left, right, 0, len(self.data) - 1)


def main():
    st = SegTree([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(st.query(4, 8))
    print(st.query(2, 3))
    print(st.query(0, 6))

    st.update(1, 5, 2)

    print(st.query(4, 8))
    print(st.query(2, 3))
    print(st.query(0, 6))


if __name__ == '__main__':
    main()
