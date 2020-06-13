#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    int T = 1;
    // cin >> T;
    while(T--) {
        char S[5001];
        cin >> S;

        int pi[5000];
        int max_cnt = 0;

        for(int i=0; i<strlen(S); i++) {
            int j = i;
            pi[i] = i;
            for(int k=i+1; k<strlen(S); k++) {
                while(S[j] != S[k] && j > i) {
                    j = pi[j-1];
                }
                if(S[j] == S[k]) {
                    pi[k] = ++j;
                } else {
                    pi[k] = i;
                }
            }

            for(int k=i; k<strlen(S); k++) {
                max_cnt = max(max_cnt, pi[k] - i);
            }
        }

        cout << max_cnt << '\n';
    }
    return 0;
}