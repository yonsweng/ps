from time import time


start_time = time()


def is_A_larger_or_equal(A, B):
    for i in range(1, len(A)):
        if A[i] < B[i]:
            return False
    return True


T = int(input())

for x in range(1, T + 1):
    N, A, B = map(int, input().split())
    U = [0] + list(map(int, input().split()))

    y = 'IMPOSSIBLE'

    for i in range(N, 1001):
        fail = False

        D = [0] * i + [1]

        for j in range(i, 0, -1):
            if j > N:
                if j-A > 0:
                    D[j-A] += D[j]
                if j-B > 0:
                    D[j-B] += D[j]
            else:
                if D[j] > U[j]:
                    if j-A > 0:
                        D[j-A] += D[j] - U[j]
                    if j-B > 0:
                        D[j-B] += D[j] - U[j]
                    D[j] = U[j]
                elif D[j] < U[j]:
                    fail = True
                    break

        if not fail:
            y = i
            break

    print(f'Case #{x}: {y}')


print(time() - start_time)
