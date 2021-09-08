t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    nas = [0] * n
    nas[0] = 1 if s[0] == 'a' else 0
    for i in range(1, n):
        if s[i] == 'a':
            nas[i] = nas[i-1] + 1
        else:
            nas[i] = nas[i-1]

    l = -1
    r = -1
    for i in range(n):
        for j in range(i, n):
            # s[i:j+1]
            n_as = nas[j] - (nas[i-1] if i-1 >= 0 else 0)
            n_total = j - i + 1
            if n_as * 2 == n_total:
                l = i + 1
                r = j + 1
                break
        if l != -1:
            break

    print(l, r)
