def main():
    n = int(input())
    a = list(map(int, input().split()))

    lis = []
    idx = []
    for i in range(n):
        if not lis or lis[-1] < a[i]:
            lis.append(a[i])
            idx.append(len(lis) - 1)
        else:
            lower, upper = 0, len(lis) - 1
            while lower < upper:
                mid = (lower + upper) // 2
                if lis[mid] < a[i]:
                    lower = mid + 1
                else:
                    upper = mid
            lis[upper] = a[i]
            idx.append(upper)

    print(len(lis))
    ans = []
    for i in range(n - 1, -1, -1):
        if idx[i] == len(lis) - 1:
            ans.append(a[i])
            lis.pop()
    ans.reverse()
    print(*ans)


if __name__ == "__main__":
    main()
