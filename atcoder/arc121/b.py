import bisect

N = int(input())

R, G, B = [], [], []

for i in range(2 * N):
    a, c = input().split()
    a = int(a)

    if c == 'R':
        R.append(a)
    elif c == 'G':
        G.append(a)
    else:
        B.append(a)


def f(A, B, C):
    A = sorted(A)  # odd
    B = sorted(B)  # odd
    C = sorted(C)  # even

    MAX = 10 ** 15
    answer = MAX
    for i in range(len(A)):
        j = bisect.bisect_left(B, A[i])
        answer = min(min(A[i] - B[j-1] if j-1 >= 0 else MAX, B[j] - A[i] if j < len(B) else MAX), answer)

    min_a, ai = MAX, 0
    for i in range(len(C)):
        j = bisect.bisect_left(A, C[i])
        min_a = min(min(C[i] - A[j-1] if j-1 >= 0 else MAX, A[j] - C[i] if j < len(A) else MAX), min_a)
        ai = i

    min_b = MAX
    for i in range(len(C)):
        if i == ai:
            continue
        j = bisect.bisect_left(B, C[i])
        min_b = min(min(C[i] - B[j-1] if j-1 >= 0 else MAX, B[j] - C[i] if j < len(B) else MAX), min_b)

    answer = min(min_a + min_b, answer)

    A, B = B, A

    min_a, ai = MAX, 0
    for i in range(len(C)):
        j = bisect.bisect_left(A, C[i])
        min_a = min(min(C[i] - A[j-1] if j-1 >= 0 else MAX, A[j] - C[i] if j < len(A) else MAX), min_a)
        ai = i

    min_b = MAX
    for i in range(len(C)):
        if i == ai:
            continue
        j = bisect.bisect_left(B, C[i])
        min_b = min(min(C[i] - B[j-1] if j-1 >= 0 else MAX, B[j] - C[i] if j < len(B) else MAX), min_b)

    answer = min(min_a + min_b, answer)

    return answer


if len(R) % 2 == 0 and len(G) % 2 == 0 and len(B) % 2 == 0:
    answer = 0
elif len(R) % 2 == 0:
    answer = f(G, B, R)
elif len(G) % 2 == 0:
    answer = f(R, B, G)
else:
    answer = f(R, G, B)

print(answer)
