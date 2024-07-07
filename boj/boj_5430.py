from sys import stdin


def solve():
    T = int(stdin.readline())
    for _ in range(T):
        p = stdin.readline().strip()
        n = int(stdin.readline())
        arr = []
        if n == 0:
            stdin.readline()
        else:
            arr = list(map(int, stdin.readline().strip()[1:-1].split(',')))
            
        left, right = 0, n - 1
        reverse = False
        error = False

        for cmd in p:
            if cmd == 'R':
                reverse = not reverse
            elif cmd == 'D':
                if left > right:
                    error = True
                    break
                if reverse:
                    right -= 1
                else:
                    left += 1

        if error:
            print('error', flush=False)
        else:
            if reverse:
                arr = arr[left:right+1][::-1]
            else:
                arr = arr[left:right+1]
            print('[' + ','.join(map(str, arr)) + ']', flush=False)


if __name__ == '__main__':
    solve()
