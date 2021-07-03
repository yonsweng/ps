t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt_odd, cnt_even = 0, 0
    for a_elt in a:
        if a_elt % 2 == 1:
            cnt_odd += 1
        else:
            cnt_even += 1

    if cnt_odd == cnt_even:
        print('Yes')
    else:
        print('No')
