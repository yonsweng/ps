from sys import stdin


class SegmentTree:
    def __init__(self, arr, start, end):
        self.arr = arr
        self.start = start
        self.end = end
        self.tree = [0] * (4 * (end - start + 1))
        self.lazy = [0] * (4 * (end - start + 1))
        self.init(1, start, end, start, end)

    def init(self, node, tl, tr, l, r):
        if tl > r or tr < l:
            return 0

        if l == r:
            self.tree[node] = self.arr[l]
            return self.tree[node]

        mid = (l + r) // 2
        self.tree[node] = self.init(node * 2, tl, tr, l, mid) + self.init(node * 2 + 1, tl, tr, mid + 1, r)
        return self.tree[node]
    
    def update(self, l, r, add):
        self.update_lazy(1, self.start, self.end, l, r, add)

    def update_lazy(self, node, tl, tr, l, r, add):
        if self.lazy[node] != 0:
            self.tree[node] += (tr - tl + 1) * self.lazy[node]
            if tl != tr:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        if tl > r or tr < l:
            return

        if l <= tl and tr <= r:
            self.tree[node] += (tr - tl + 1) * add
            if tl != tr:
                self.lazy[node * 2] += add
                self.lazy[node * 2 + 1] += add
            return

        mid = (tl + tr) // 2
        self.update_lazy(node * 2, tl, mid, l, r, add)
        self.update_lazy(node * 2 + 1, mid + 1, tr, l, r, add)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, l, r):
        return self.query_lazy(1, self.start, self.end, l, r)
    
    def query_lazy(self, node, tl, tr, l, r):
        if self.lazy[node] != 0:
            self.tree[node] += (tr - tl + 1) * self.lazy[node]
            if tl != tr:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        if tl > r or tr < l:
            return 0

        if l <= tl and tr <= r:
            return self.tree[node]

        mid = (tl + tr) // 2
        return self.query_lazy(node * 2, tl, mid, l, r) + self.query_lazy(node * 2 + 1, mid + 1, tr, l, r)


def main():
    N = int(stdin.readline())
    A = [0] + list(map(int, stdin.readline().split()))
    Q = int(stdin.readline())

    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = A[i] - A[i - 1]

    st = SegmentTree(B, 1, N)

    for _ in range(Q):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            l, r = query[1], query[2]
            st.update(l, r, 1)
            st.update(r + 1, r + 1, -r + l - 1)
        else:
            k = query[1]
            print(st.query(1, k), flush=False)


if __name__ == "__main__":
    main()


"""
5
1 2 1 2 1
4
1 1 5
2 5
1 2 5
2 5

5
1 2 1 2 1
8
1 1 1
2 1
1 2 5
2 4
1 2 3
2 2
2 1
2 3

"""