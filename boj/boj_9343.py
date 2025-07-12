from sys import stdin

MOD = 1000000007
MAX_N = 1000000

# Precompute all Catalan numbers up to MAX_N
catalan_numbers = [0] * (MAX_N + 1)

def precompute_catalan():
    catalan_numbers[0] = 1
    catalan_numbers[1] = 1
    
    for i in range(2, MAX_N + 1):
        # C(n) = C(n-1) * 2 * (2*n - 1) / (n + 1)
        catalan_numbers[i] = (catalan_numbers[i-1] * 2 * (2 * i - 1)) % MOD
        inv = pow(i + 1, MOD - 2, MOD)  # Modular inverse using Fermat's little theorem
        catalan_numbers[i] = (catalan_numbers[i] * inv) % MOD


def main():
    precompute_catalan()
    
    T = int(stdin.readline().strip())
    for _ in range(T):
        N = int(stdin.readline().strip())
        print(catalan_numbers[N], flush=False)


if __name__ == "__main__":
    main()
