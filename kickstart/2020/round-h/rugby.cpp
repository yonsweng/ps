#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        ll y = 0;

        int N;
        cin >> N;
        vector<int> X(N + 1), Y(N + 1);
        for (int i = 1; i <= N; i++) {
            cin >> X[i] >> Y[i];
        }

        sort(Y.begin() + 1, Y.end());
        int Ym = N % 2 == 1 ? Y[(N + 1) / 2] : (Y[N / 2] + Y[N / 2 + 1]) / 2;
        for (int i = 1; i <= N; i++) {
            y += abs(Y[i] - Ym);
        }

        sort(X.begin() + 1, X.end());
        vector<int> move(N);
        for (int k = 0; k < N; k++) {
            move[k] = k - X[k+1];
        }
        sort(move.begin(), move.end());
        int Xm = -move[N/2];
        for(int i=1; i<=N; i++) {
            y += abs((ll)Xm + (i - 1) - X[i]);
        }

        cout << "Case #" << x << ": " << y << '\n';
    }

    return 0;
}