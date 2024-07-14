from sys import stdin

n, m = map(int, stdin.readline().split())
pokemons = {}
for i in range(1, n + 1):
    pokemon = stdin.readline().strip()
    pokemons[pokemon] = i
    pokemons[i] = pokemon

for _ in range(m):
    query = stdin.readline().strip()
    if query.isdigit():
        print(pokemons[int(query)], flush=False)
    else:
        print(pokemons[query], flush=False)
