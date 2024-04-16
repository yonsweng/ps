from sys import stdin


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, x):
        while i <= self.n:
            self.tree[i] += x
            i += i & -i

    def range_update(self, l, r, x):
        self.update(l, x)
        self.update(r + 1, -x)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res
    
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)



def main():
    N = int(stdin.readline())
    A = [0] + list(map(int, stdin.readline().split()))
    Q = int(stdin.readline())

    lt = FenwickTree(N)
    ct = FenwickTree(N)

    for _ in range(Q):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            l, r = query[1], query[2]
            lt.range_update(l, r, l)
            ct.range_update(l, r, 1)
        else:
            k = query[1]
            l = lt.query(k)
            c = ct.query(k)
            answer = A[k] - l + c * (k + 1)
            print(answer, flush=False)


if __name__ == "__main__":
    main()
