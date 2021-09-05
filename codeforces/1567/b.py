T = int(input())

cur = 0
d = []
for c in range(300000):
    cur ^= c
    d.append(cur)


for _ in range(T):
    a, b = map(int, input().split())

    e = d[a-1]

    # print('d:', d)
    # print('d^a:', d^a)

    if e == b:
        answer = a
    elif (e ^ b) == a:
        answer = a + 2
    else:
        answer = a + 1

    print(answer)
