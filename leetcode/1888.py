class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        evenN = (n + 1) // 2
        oddN = n // 2

        evenZero, evenOne, oddZero, oddOne = 0, 0, 0, 0

        for i in range(0, n, 2):
            if s[i] == '0':
                evenZero += 1
            else:
                evenOne += 1
        for i in range(1, n, 2):
            if s[i] == '0':
                oddZero += 1
            else:
                oddOne += 1

        answer = min(evenN - evenZero + oddN - oddOne, evenN - evenOne + oddN - oddZero)
        for i in range(n-1):
            if n % 2 == 0:
                evenZero, evenOne, oddZero, oddOne = oddZero, oddOne, evenZero, evenOne
            else:
                if s[i] == '0':
                    evenZero, evenOne, oddZero, oddOne = oddZero + 1, oddOne, evenZero - 1, evenOne
                else:
                    evenZero, evenOne, oddZero, oddOne = oddZero, oddOne + 1, evenZero, evenOne - 1

            tmp_answer = min(evenN - evenZero + oddN - oddOne, evenN - evenOne + oddN - oddZero)
            answer = min(answer, tmp_answer)

        return answer
