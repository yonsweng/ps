T = int(input())
for i in range(1, T+1):
    N = int(input())
    W = input()
    X = []
    for w in W:
        if w != 'F':
            X.append(w)
    X = ''.join(X)
    answer = 0
    for j in range(len(X)-1):
        if X[j] != X[j+1]:
            answer += 1
    print(f'Case #{i}: {answer}')
