#include <iostream>
#include <string>

#define MAX 9223372036854775807LL

using namespace std;

int to_num(char c) {
    if(c >= '0' && c <= '9')
        return c - '0';
    else
        return c - 'a' + 10;
}

int main() {
    string P, S;
    cin >> P >> S;

    int minA = 2, minB = 2;
    for(char c : P) {
        minA = max(minA, to_num(c) + 1);
    }
    for(char c : S) {
        minB = max(minB, to_num(c) + 1);
    }

    int n_answers = 0, answerX, answerA, answerB;
    for(int A = minA; A <= 36; A++) {
        for(int B = minB; B <= 36; B++) {
            if(A == B)
                continue;

            bool overflow = false;

            long long X1 = 0, power1 = 1;
            for(int i = P.size() - 1; i >= 0 && (to_num(P[i]) == 0 || power1 <= MAX / to_num(P[i])); i--, power1 *= A) {
                if(X1 > MAX - power1 * to_num(P[i])) {
                    overflow = true;
                    break;
                }
                X1 += power1 * to_num(P[i]);
            }

            long long X2 = 0, power2 = 1;
            for(int i = S.size() - 1; i >= 0 && (to_num(P[i]) == 0 || power2 <= MAX / to_num(S[i])); i--, power2 *= B) {
                if(X2 > MAX - power2 * to_num(S[i])) {
                    overflow = true;
                    break;
                }
                X2 += power2 * to_num(S[i]);
            }

            if(!overflow && X1 == X2) {
                n_answers++;
                answerX = X1;
                answerA = A;
                answerB = B;
                // cout << answerX << ' ' << answerA << ' ' << answerB << '\n';
            }
        }
    }

    if(n_answers == 0)
        cout << "Impossible";
    else if(n_answers == 1)
        cout << answerX << ' ' << answerA << ' ' << answerB;
    else
        cout << "Multiple";
}