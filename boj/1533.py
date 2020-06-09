import math

DIV: int = 1000003


def matmul(a, b):
    aw = a[0].__len__()
    ah = a.__len__()
    bw = b[0].__len__()
    c = [[0] * bw for i in range(ah)]
    for i in range(ah):
        for j in range(bw):
            c[i][j] = sum([(a[i][k] % DIV) * (b[k][j] % DIV) % DIV for k in range(aw)])

    return c


n, s, e, t = [int(num) for num in input().split()]
s -= 1
e -= 1
graph = [[0] * n for i in range(n)]

for i in range(n):
    line = input()
    for j in range(n):
        graph[i][j] = int(line[j])

cnt = n
for i in range(n):
    for j in range(n):
        if graph[i][j] > 1:
            cnt += graph[i][j] - 1

d = [[0] * cnt for i in range(cnt)]

new = n
for i in range(n):
    for j in range(n):
        if graph[i][j] > 1:
            former = i
            for k in range(1, graph[i][j]):
                d[former][new] = 1
                former = new
                new += 1
            d[former][j] = 1
        else:
            d[i][j] = graph[i][j]

# t를 이진수로 바꾸는 작업
# b[0] : 2^0 자리, ...
m = []
b = []
t0: int = t
while t0 > 0:
    b.append(t0 % 2)
    t0 = int(t0 / 2)
    m.append(d)
    d = matmul(d, d)

identity = [[0] * cnt for i in range(cnt)]
for i in range(cnt):
    identity[i][i] = 1

ret = identity

for l in range(m.__len__()):
    if b[l]:
        ret = matmul(ret, m[l])

print(ret[s][e] % DIV)

'''9 1 3 100000000
012341232
102312312
230431021
123042314
402301234
123430132
012304021
203234005
012340020

answer = 872914
'''