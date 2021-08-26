one = ['1', '4', '6', '8', '9']
two = ['22', '25', '27', '32', '33', '35', '52', '55', '57', '72', '75', '77']
# three = ['537', '573']

t = int(input())

for _ in range(t):
    k = int(input())
    n = input()

    answer = ''

    for lst in (one, two):
        for composite in lst:
            p_composite = 0
            for digit_of_n in n:
                if digit_of_n == composite[p_composite]:
                    p_composite += 1
                    if p_composite == len(composite):
                        answer = composite
                        break
            if answer != '':
                break
        if answer != '':
            break

    print(len(answer))
    print(answer)
