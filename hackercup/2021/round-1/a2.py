T = int(input())
for i in range(1, T+1):
    N = int(input())
    W = input()
    X = []
    Y = []
    for j, w in enumerate(W):
        if w != 'F':
            X.append(w)
            Y.append(j)
    X = ''.join(X)
    answer = 0
    for j in range(len(X)-1):
        if X[j] != X[j+1]:
            answer = (answer + (Y[j] + 1) * (N - Y[j+1])) % 1000000007
    print(f'Case #{i}: {answer}')
