t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for i, c in enumerate(s):
        if c != '0':
            if i != len(s) - 1:
                cnt += 1
            cnt += ord(c) - ord('0')

    print(cnt)
