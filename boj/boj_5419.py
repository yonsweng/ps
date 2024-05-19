from sys import stdin


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, diff):
        if idx < start or idx > end:
            return

        self.tree[node] += diff
        if start == end:
            return

        mid = (start + end) // 2
        self.update(node * 2, start, mid, idx, diff)
        self.update(node * 2 + 1, mid + 1, end, idx, diff)

    def query(self, node, ts, te, qs, qe):
        if qe < ts or te < qs:
            return 0
        if qs <= ts and te <= qe:
            return self.tree[node]

        mid = (ts + te) // 2
        return self.query(node * 2, ts, mid, qs, qe) + self.query(node * 2 + 1, mid + 1, te, qs, qe)


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        points = []
        for _ in range(n):
            x, y = map(int, stdin.readline().split())
            points.append((x, y))

        points.sort(key=lambda x: (x[0], -x[1]))

        # coordinate compression
        x_values = [x for x, _ in points]
        y_values = [y for _, y in points]
        x_values = {x: i for i, x in enumerate(sorted(set(x_values)))}
        y_values = {y: i for i, y in enumerate(sorted(set(y_values)))}
        points = [(x_values[x], y_values[y]) for x, y in points]

        max_y = max(y_values.values())

        st = SegmentTree(len(y_values))
        result = 0
        for _, y in points:
            result += st.query(1, 0, len(y_values) - 1, y, max_y)
            st.update(1, 0, len(y_values) - 1, y, 1)

        print(result, flush=False)


if __name__ == "__main__":
    main()
