from sys import stdin


# min segment tree
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [float("inf")] * (n * 4)

    def _update(self, node, start, end, index, value):
        if index < start or end < index:
            return
        if start == end:
            self.tree[node] = min(self.tree[node], value)
            return

        mid = (start + end) // 2
        self._update(node * 2, start, mid, index, value)
        self._update(node * 2 + 1, mid + 1, end, index, value)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return float("inf")
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return min(
            self._query(node * 2, start, mid, left, right),
            self._query(node * 2 + 1, mid + 1, end, left, right),
        )

    def update(self, index, value):
        self._update(1, 1, self.n, index, value)

    def query(self, left, right):
        return self._query(1, 1, self.n, left, right)


def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))

    contestants = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        contestants[a[i] - 1][0] = i + 1
        contestants[b[i] - 1][1] = i + 1
        contestants[c[i] - 1][2] = i + 1
    contestants.sort(key=lambda x: x[0])

    answer = 0
    st = SegmentTree(n + 1)
    for _, b, c in contestants:
        if st.query(1, b) > c:
            answer += 1
        st.update(b, c)
    print(answer)


if __name__ == "__main__":
    solve()
