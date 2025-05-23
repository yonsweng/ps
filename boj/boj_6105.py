from sys import stdin


def solve():
    N = int(stdin.readline())
    H = [0]
    for _ in range(N):
        H.append(int(stdin.readline()))

    stack = []
    answer = [0] * (N + 1)
    for i in range(1, N + 1):
        while stack:
            top = stack[-1]
            if H[top] < H[i]:
                answer[top] = i
                stack.pop()
            else:
                break
        stack.append(i)

    print("\n".join(map(str, answer[1:])))


if __name__ == "__main__":
    solve()
