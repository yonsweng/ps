class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n * 4)

    def _update(self, node, start, end, i, v):
        if i < start or end < i:
            return self.tree[node]
        if start == end:
            self.tree[node] += v
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = self._update(node * 2, start, mid, i, v) + self._update(
            node * 2 + 1, mid + 1, end, i, v
        )
        return self.tree[node]

    def update(self, i, v):
        return self._update(1, 0, self.n - 1, i, v)

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self._query(node * 2, start, mid, left, right) + self._query(
            node * 2 + 1, mid + 1, end, left, right
        )

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)


def main():
    n = int(input())
    a = list(map(int, input().split()))

    # coordinate compression
    c = {v: i for i, v in enumerate(sorted(set(a)))}
    a = [c[v] for v in a]

    ma = max(a)
    st = SegmentTree(ma + 1)
    answer = 0
    for ai in a:
        answer += st.query(ai + 1, ma)
        st.update(ai, 1)

    print(answer)


if __name__ == "__main__":
    main()
