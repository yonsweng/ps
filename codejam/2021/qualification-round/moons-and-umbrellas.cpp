#include <bits/stdc++.h>

#define INF 99900

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for(int x = 1; x <= T; x++) {
        int X, Y;
        char S[1001];
        cin >> X >> Y >> S;

        int N = strlen(S);
        int D[1000][2];
        for(int i=0; i<N; i++) {
            D[i][0] = D[i][1] = 2 * INF;
        }
        if(S[0] == 'C') D[0][0] = 0;
        else if(S[0] == 'J') D[0][1] = 0;
        else D[0][0] = D[0][1] = 0;

        for(int i=1; i<N; i++) {
            if(S[i] == 'C') {
                D[i][0] = min(D[i-1][0], D[i-1][1] + Y);
            } else if(S[i] == 'J') {
                D[i][1] = min(D[i-1][1], D[i-1][0] + X);
            } else {
                D[i][0] = min(D[i-1][0], D[i-1][1] + Y);
                D[i][1] = min(D[i-1][1], D[i-1][0] + X);
            }
        }

        int y = min(D[N-1][0], D[N-1][1]);
        cout << "Case #" << x << ": " << y << '\n';
    }
}