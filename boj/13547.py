from bisect import bisect_left
from collections.abc import Iterable
from sys import stdin


class TreeNode:
    def __init__(self, e: Iterable[int], l, r):
        self.e = list(e)
        self.l = l
        self.r = r


class MergeSortTree:
    def __init__(self, a: Iterable[int]):
        self.a = a
        self.n = len(a)
        self.nodes = [None] * (4 * self.n)
        self._init(0, 0, self.n - 1)

    def _merge(self, a: Iterable[int], b: Iterable[int]) -> list:
        c = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        while i < len(a):
            c.append(a[i])
            i += 1
        while j < len(b):
            c.append(b[j])
            j += 1
        return c

    def _init(self, i, l, r):
        if l == r:
            self.nodes[i] = TreeNode([self.a[l]], l, r)
            return
        m = (l + r) // 2
        self._init(2 * i + 1, l, m)
        self._init(2 * i + 2, m + 1, r)
        self.nodes[i] = TreeNode(
            self._merge(self.nodes[2 * i + 1].e, self.nodes[2 * i + 2].e), l, r
        )

    def _query(self, i, l, r, k):
        if r < self.nodes[i].l or self.nodes[i].r < l:
            return 0
        if l <= self.nodes[i].l and self.nodes[i].r <= r:
            return (self.nodes[i].r - self.nodes[i].l + 1) - bisect_left(
                self.nodes[i].e, k
            )
        return self._query(2 * i + 1, l, r, k) + self._query(2 * i + 2, l, r, k)

    def query(self, l, r, k):
        return self._query(0, l, r, k)


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

b = [n] * n
leftmost_idx = {}
for i in range(n - 1, -1, -1):
    if a[i] in leftmost_idx:
        b[i] = leftmost_idx[a[i]]
    leftmost_idx[a[i]] = i

t = MergeSortTree(b)
m = int(stdin.readline())
for _ in range(m):
    l, r = map(int, stdin.readline().split())
    print(t.query(l - 1, r - 1, r), flush=False)
