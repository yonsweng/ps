n = int(input())
a = [int(num) for num in input().split()]
# [10, 20, 10, 30, 20, 50]
# 가장 긴 증가하는 부분 수열
# [10, 20, 30, 50]
d = [1]
for i in range(1, n):
    m = 0
    for j in range(i):
        if a[i] > a[j] and d[j] > m:
            m = d[j]

    d.append(m + 1)

print(max(d))
