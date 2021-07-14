def count_blocks(s):
    n_blocks = 0
    prev = '2'
    for c in s:
        if prev != c:
            n_blocks += 1
            prev = c
    return n_blocks


t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()

    n_blocks = count_blocks(s)

    if b < 0:
        answer = (n_blocks // 2 + 1) * b + n * a
    else:
        answer = n * b + n * a

    print(answer)
