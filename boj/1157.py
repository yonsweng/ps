d = {}
a = input().lower()
for c in a:
    d[c] = d.get(c, 0) + 1
s = sorted(d.items(), key=lambda x: x[1], reverse=True)
if len(s) > 1 and s[0][1] == s[1][1]:
    print('?')
else:
    print(s[0][0].upper())
