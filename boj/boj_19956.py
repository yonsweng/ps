from collections import deque
from sys import stdin


def prime_factorization(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors


def count_common_prime_factors(np, mp):
    common_factors = 0
    for prime in np:
        if prime in mp:
            common_factors += 1
    return common_factors


def bfs(np_factors, mp_factors):
    queue = deque([(np_factors.copy(), [])])  # (current_factors, operations_path)
    visited = set()
    visited.add(tuple(sorted(np_factors.items())))
    
    while queue:
        current_factors, path = queue.popleft()
        
        if current_factors == mp_factors:
            return path
        
        # Check if we can multiply by 2 (operation 0)
        can_multiply = True
        for prime in current_factors:
            if current_factors.get(prime, 0) > mp_factors.get(prime, 0):
                can_multiply = False
                break
        
        if can_multiply:
            new_factors = current_factors.copy()
            # Double all prime factor counts
            for prime in list(new_factors.keys()):
                new_factors[prime] *= 2
            new_tuple = tuple(sorted(new_factors.items()))
            if new_tuple not in visited:
                visited.add(new_tuple)
                queue.append((new_factors, path + [0]))
        
        # Try dividing by each prime p where count >= 1
        for prime in list(current_factors.keys()):
            if current_factors[prime] >= 1:
                new_factors = current_factors.copy()
                new_factors[prime] -= 1
                if new_factors[prime] == 0:
                    del new_factors[prime]
                new_tuple = tuple(sorted(new_factors.items()))
                if new_tuple not in visited:
                    visited.add(new_tuple)
                    queue.append((new_factors, path + [prime]))
    
    return None  # No solution found


def solve():
    n, m = map(int, stdin.readline().split())
    
    np = prime_factorization(n)
    mp = prime_factorization(m)
    
    np_nonzero = len(np)
    mp_nonzero = len(mp)
    
    if np_nonzero < mp_nonzero:
        print("Impossible")
        return
    
    result = bfs(np, mp)
    
    if result is not None:
        print(" ".join(map(str, result)))
    else:
        print("Impossible")


if __name__ == "__main__":
    solve()
