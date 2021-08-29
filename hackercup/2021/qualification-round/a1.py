from collections import Counter
from string import ascii_uppercase

VOWELS = ['A', 'E', 'I', 'O', 'U']

T = int(input())

for i in range(1, T + 1):
    S = input()

    cnt = Counter(S)
    n_vowels = sum(cnt[vowel] for vowel in VOWELS)
    n_consonants = len(S) - n_vowels

    answer = 2 * len(S)  # max possible answer

    for alphabet in ascii_uppercase:
        if alphabet in VOWELS:
            answer = min(n_consonants + 2 * (n_vowels - cnt[alphabet]), answer)
        else:
            answer = min(2 * (n_consonants - cnt[alphabet]) + n_vowels, answer)

    print(f'Case #{i}: {answer}')
