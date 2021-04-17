n, p = map(int, input().split())

answer = (p - 1) * pow(p - 2, n - 1, 1000000007) % 1000000007

print(answer)
