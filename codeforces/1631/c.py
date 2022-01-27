from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        a = list(range(n//2))
        b = list(range(n-1, n//2, -1))

        if n == 4:
            if k == 3:
                print(-1)
            else:
                print(f"3 {k}")
                s = set(range(4))
                s.remove(3)
                s.remove(k)
                print(f"{s.pop()} {s.pop()}")
        else:
            if k == n - 1:
                print(f"{k} {k-1}")
                print(f"1 3")
                s = set([k, k-1, 1, 3, 0, n-4])
                for i in range(2, k-1):
                    if i not in s and (n-i-1) not in s:
                        print(f"{i} {n-i-1}")
                        s.add(i)
                        s.add(n-i-1)
                print(f"0 {n-4}")
            else:
                print(f"{n-1} {k}")
                for i in range(1, n//2):
                    if i != k and n-i-1 != k:
                        print(f"{i} {n-i-1}")
                if k != 0:
                    print(f"0 {n-k-1}")


if __name__ == '__main__':
    main()
