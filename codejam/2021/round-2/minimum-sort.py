T, N = map(int, input().split())

for x in range(1, T + 1):
    for i in range(1, N):
        print(f'M {i} {N}', flush=True)
        pos = int(input())
        if i != pos:
            print(f'S {i} {pos}', flush=True)
            judge = int(input())
    print('D', flush=True)
    judge = int(input())
