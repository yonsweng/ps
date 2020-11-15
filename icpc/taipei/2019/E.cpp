#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    while (T--) {
        long long k, L, N, a;
        cin >> k >> L;
        if (L >= 2000 || L == 1) {
            cout << -1 << '\n';
            continue;
        }
        N = L;
        a = 1000000;
        // (N - 1) * 10^6 - N * alpha = K
        // N * alpha = (N - 1) * 10^6 - K
        long long S = ((N - 1) * a - k) / N;
        long long S2 = ((N - 1) * a - k) - N * S;

        long long Q, R;
        Q = S / (N - 1);
        R = S - Q * (N - 1);
        vector<long long> ans(N, -Q);
        ans[N - 1] = a;
        for (int i = 0; i < R; i++) {
            ans[i]--;
        }


        if ((N - 1) * 1000000 < S) {
            cout << -1 << '\n';
            continue;
        }

        cout << N << '\n';
        for (auto k : ans) cout << k << ' ';
        cout << '\n';
    }
}