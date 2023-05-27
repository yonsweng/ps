x = int(input())

for s in range(1, 10010):
    if s * (s - 1) >= x * 2:
        break

s -= 1

t = x - s * (s - 1) // 2

if s % 2 == 0:
    print(f"{t}/{s + 1 - t}")
else:
    print(f"{s + 1 - t}/{t}")
