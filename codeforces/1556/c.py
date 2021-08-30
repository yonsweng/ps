n = int(input())
a = list(map(int, input().split()))

s = []

answer = 0

for i in range(n):
    if i % 2 == 0:
        if len(s) == 0 or s[-1][0] != '(':
            s.append(['(', a[i]])
        else:
            s[-1][1] += a[i]
    else:
        while len(s) > 0:
            if len(s) > 0 and s[-1][0] == '(':
                if s[-1][1] <= a[i]:
                    a[i] -= s[-1][1]
                    s[-1][0] = '()'
                else:
                    s[-1][1] -= a[i]
                    s.append(['()', a[i]])
                    a[i] = 0

            if a[i] == 0:
                break

            accu = 0
            while len(s) > 0 and s[-1][0] == '()':
                answer += s[-1][1] + accu
                s.pop()
                accu += 1

accu = 0
while len(s) > 0:
    if s[-1][0] == '()':
        answer += s[-1][1] + accu
        accu += 1
        s.pop()
    else:
        accu = 0
        s.pop()

print(answer)

'''
6
1 2 4 5 3 3

8

5
4 1 2 3 1

5

6
1 1 1 1 2 2

7

'''
