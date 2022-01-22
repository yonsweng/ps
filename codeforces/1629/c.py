from sys import stdin
from collections import deque


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))

        q = {i: deque() for i in range(n+2)}
        for i, ai in enumerate(a):
            q[ai].append(i)

        left = 0
        mex = []
        while len(q[0]):
            right = -1
            for i in range(n+2):
                while len(q[i]) and q[i][0] < left:
                    q[i].popleft()
                if len(q[i]):
                    right = max(right, q[i].popleft())
                else:
                    break
            if right == -1:
                break
            mex.append(i)
            left = right + 1
        for i in range(n+1):
            while len(q[i]):
                if left <= q[i][0]:
                    mex.append(0)
                q[i].popleft()
        print(len(mex))
        print(' '.join(map(str, mex)))


if __name__ == '__main__':
    main()
