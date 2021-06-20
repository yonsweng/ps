n, q = map(int, input().split())
s = input()

indice = [ord(c) - ord('a') + 1 for c in s]
for i in range(1, len(indice)):
    indice[i] += indice[i-1]


def question(l, r):
    return indice[r-1] - (indice[l-2] if l >= 2 else 0)


for _ in range(q):
    l, r = map(int, input().split())
    print(question(l, r))
