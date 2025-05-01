a, b = map(int, input().split())

ai, aj = (a - 1) % 4, (a - 1) // 4
bi, bj = (b - 1) % 4, (b - 1) // 4

print(abs(ai - bi) + abs(aj - bj))
