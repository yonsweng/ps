#include <iostream>

using namespace std;

int G[1002][1002];
int W[1002][1002];
int E[1002][1002];
int N[1002][1002];
int S[1002][1002];
// int D[1002][1002];

int main() {
    // freopen("1.in", "r", stdin);

    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        int R, C;
        cin >> R >> C;
        for(int i=1; i<=R; i++) {
            for(int j=1; j<=C; j++) {
                cin >> G[i][j];
                // D[i][j] = 0;
            }
            G[i][C+1] = E[i][C+1] = 0;
        }
        for(int j=1; j<=C; j++) {
            G[R+1][j] = S[R+1][j] = 0;
        }

        for(int i=1; i<=R; i++)
            for(int j=1; j<=C; j++)
                if(G[i][j]) W[i][j] = W[i][j-1] + 1;
                else W[i][j] = 0;
        for(int i=1; i<=R; i++)
            for(int j=C; j>=1; j--)
                if(G[i][j]) E[i][j] = E[i][j+1] + 1;
                else E[i][j] = 0;
        for(int j=1; j<=C; j++)
            for(int i=1; i<=R; i++)
                if(G[i][j]) N[i][j] = N[i-1][j] + 1;
                else N[i][j] = 0;
        for(int j=1; j<=C; j++)
            for(int i=R; i>=1; i--)
                if(G[i][j]) S[i][j] = S[i+1][j] + 1;
                else S[i][j] = 0;

        int y = 0;

        for(int i=1; i<=R; i++) {
            for(int j=1; j<=C; j++) {
                // WN
                if(W[i][j] >= 2 && N[i][j] >= 2) {
                    int m = min(W[i][j], N[i][j]);
                    int M = max(W[i][j], N[i][j]);
                    y += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                    // D[i][j] += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                }
                // WS
                if(W[i][j] >= 2 && S[i][j] >= 2) {
                    int m = min(W[i][j], S[i][j]);
                    int M = max(W[i][j], S[i][j]);
                    y += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                    // D[i][j] += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                }
                // EN
                if(E[i][j] >= 2 && N[i][j] >= 2) {
                    int m = min(E[i][j], N[i][j]);
                    int M = max(E[i][j], N[i][j]);
                    y += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                    // D[i][j] += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                }
                // ES
                if(E[i][j] >= 2 && S[i][j] >= 2) {
                    int m = min(E[i][j], S[i][j]);
                    int M = max(E[i][j], S[i][j]);
                    y += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                    // D[i][j] += min(m - 1, M / 2 - 1) + min(M - 1, m / 2 - 1);
                }
                // cout << D[i][j] << ' ';
            }
            // cout << '\n';
        }

        cout << "Case #" << x << ": " << y << '\n';
    }
}