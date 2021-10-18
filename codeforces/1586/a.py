from sys import stdin


def read_input():
    n = int(stdin.readline())                     # read an integer.
    a = list(map(int, stdin.readline().split()))  # read several integers of a line.
    return n, a


def is_prime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n%2==0 or n%3==0:
		return False
	i = 5
	while i**2 <= n:
		if n%i==0 or n%(i+2)==0:
			return False
		i = i + 6
	return True


def find_one(a):
    sa = sorted([(ai, i) for i, ai in enumerate(a)])
    for ai, i in sa:
        if ai % 2 == 1:
            return i
    return -1


def solve(n, a):
    s = sum(a)
    if not is_prime(s):
        answer = str(n) + '\n' + ' '.join(map(str, list(range(1, n + 1))))
    else:
        index_of_one = find_one(a) + 1
        answer = str(n-1) + '\n' + ' '.join(map(str, [i for i in range(1, n + 1) if i != index_of_one]))

    return answer


def main():
    t = int(stdin.readline())

    for _ in range(t):
        input = read_input()
        answer = solve(*input)
        print(answer)


if __name__ == '__main__':
    main()
