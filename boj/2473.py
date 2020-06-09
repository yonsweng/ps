'''
백준 온라인 저지 2473 세 용액 문제
5
-2 6 -97 -6 98

-97 -2 98
'''

n = int(input())
line = input()
d = [int(token) for token in line.split()]

result = [0, 0, 0]
m = 2000000000
for i in range(n-2):
    for j in range(i+1, n-1):
        sum_two = d[i] + d[j]
        left = j + 1
        right = n
        while left < right:
            center = int((left + right) / 2)
            s = sum_two + d[center]
            if abs(s) < m:
                m = abs(s)
                result[0] = d[i]
                result[1] = d[j]
                result[2] = d[center]
            if s < 0:
                right = center
            else:
                left = center + 1

result.sort()
print("%d %d %d" % (result[0], result[1], result[2]))
