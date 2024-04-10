"""
3
10 10 20 20
15 15 25 30
18 18 27 27

2
10 10 20 20
15 15 25 30
"""

from sys import stdin


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.cnt = [0] * (4 * n)
        self.area = [0] * (4 * n)
        
    def update_range(self, node, start, end, left, right, diff):
        if right < start or end < left:
            return
        if left <= start and end <= right:
            self.cnt[node] += diff
        else:
            mid = (start + end) // 2
            self.update_range(node * 2, start, mid, left, right, diff)
            self.update_range(node * 2 + 1, mid + 1, end, left, right, diff)

        if self.cnt[node] > 0:
            self.area[node] = end - start + 1
        else:
            if start == end:
                self.area[node] = 0
            else:
                self.area[node] = self.area[node * 2] + self.area[node * 2 + 1]


def main():
    MAX = 30000

    delta = []
    n = int(stdin.readline())
    for _ in range(n):
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        delta.append((y1, 1, x1, x2))
        delta.append((y2, -1, x1, x2))
    delta.sort()

    ans = 0
    prev_y = 0
    st = SegmentTree(MAX)
    for y, d, x1, x2 in delta:
        ans += st.area[1] * (y - prev_y)
        st.update_range(1, 0, MAX - 1, x1, x2 - 1, d)
        prev_y = y

    print(ans)


if __name__ == "__main__":
    main()
