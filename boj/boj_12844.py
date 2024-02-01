from sys import stdin


class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def init(self, a, node, start, end):
        if start == end:
            self.tree[node] = a[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = self.init(a, node * 2, start, mid) ^ self.init(
            a, node * 2 + 1, mid + 1, end
        )
        return self.tree[node]

    def update_lazy(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] ^= self.lazy[node] * int((end - start + 1) % 2)
            if start != end:
                self.lazy[node * 2] ^= self.lazy[node]
                self.lazy[node * 2 + 1] ^= self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, node, start, end, left, right, k):
        self.update_lazy(node, start, end)

        if right < start or end < left:
            return

        if left <= start and end <= right:
            self.tree[node] ^= k * int((end - start + 1) % 2)
            if start != end:
                self.lazy[node * 2] ^= k
                self.lazy[node * 2 + 1] ^= k
            return

        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, left, right, k)
        self.update_range(node * 2 + 1, mid + 1, end, left, right, k)
        self.tree[node] = self.tree[node * 2] ^ self.tree[node * 2 + 1]

    def query(self, node, start, end, left, right):
        self.update_lazy(node, start, end)

        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self.query(node * 2, start, mid, left, right) ^ self.query(
            node * 2 + 1, mid + 1, end, left, right
        )


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    seg = SegmentTree(n)
    seg.init(a, 1, 0, n - 1)

    m = int(stdin.readline())
    for _ in range(m):
        line = map(int, stdin.readline().split())
        if next(line) == 1:
            i, j, k = line
            seg.update_range(1, 0, n - 1, i, j, k)
        else:
            i, j = line
            print(seg.query(1, 0, n - 1, i, j), flush=False)


if __name__ == "__main__":
    main()
