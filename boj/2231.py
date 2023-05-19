def solution(n):
    for i in range(1, n):
        if n == i + sum(map(int, str(i))):
            print(i)
            return
    print(0)


n = int(input())
solution(n)
