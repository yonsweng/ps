def main():
    T = int(input())
    for x in range(T):
        M = int(input())
        P, N = [], []
        for _ in range(M):
            p, n = (int(a) for a in input().split())
            P.append(p)
            N.append(n)

        S = 0
        for i in range(M):
            S += P[i] * N[i]

        y = 0
        D = {1: S}
        for j, p in enumerate(P):
            keys = list(D.keys())
            for key in keys:
                d = D[key]
                n = 1
                for i in range(1, N[j]+1):
                    n *= p
                    if key * n > d - p * i:
                        break
                    if key * n == d - p * i:
                        y = max(y, key * n)
                    D[key * n] = d - p * i
        
        print(f'Case #{x}: {y}')


if __name__ == '__main__':
    main()
