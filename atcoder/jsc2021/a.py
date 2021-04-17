import math
x, y, z = map(int, input().split())
print(math.ceil(y*z/x)-1)