from sys import stdin

def dfs(idx, cnt, l, c, password):
    if cnt == l:
        consonant = 0
        vowel = 0
        for i in password:
            if i in 'aeiou':
                vowel += 1
            else:
                consonant += 1
        if consonant >= 2 and vowel >= 1:
            print(password)
        return
    if idx == c:
        return
    dfs(idx+1, cnt+1, l, c, password+alpha[idx])
    dfs(idx+1, cnt, l, c, password)

l, c = map(int, stdin.readline().split())
alpha = sorted(list(stdin.readline().split()))
dfs(0, 0, l, c, '')
