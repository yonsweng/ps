def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input()
        b = input()
        i = 0
        answer = 0
        a += a[-1]
        b += b[-1]
        while i < n:
            if a[i] == '0' and b[i] == '0':
                if a[i+1] == '1' and b[i+1] == '1':
                    answer += 2
                    i += 2
                else:
                    answer += 1
                    i += 1
            elif a[i] == '1' and b[i] == '1':
                if a[i+1] == '0' and b[i+1] == '0':
                    answer += 2
                    i += 2
                else:
                    i += 1
            else:
                answer += 2
                i += 1
        print(answer)


if __name__ == '__main__':
    main()
