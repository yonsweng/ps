#include <bits/stdc++.h>

using namespace std;

int dp[3][10000];

int main() {
    // freopen("input/1.in", "r", stdin);
    int n;
    string S, T;
    int i, j;
    cin >> n;  // 3 <= n <= 10,000
    cin >> S;
    cin >> T;
    cin >> i >> j;

    string S1, S2;
    for(int k=0; k<n; k++) {
        if(k == i || k == j) {
            S2.push_back(S[k]);
        } else {
            S1.push_back(S[k]);
        }
    }

    for(int k=0; k<3; k++) {
        for(int l=0; l<n; l++) {
            bool a, b, c, d;
            a = l > 0 ? dp[k][l-1] : true;
            b = l - k >= 0 ? S1[l-k] == T[l] : false;
            c = (k > 0 && l > 0) ? dp[k-1][l-1] : true;
            d = k > 0 ? S2[k-1] == T[l] : false;

            dp[k][l] = (a && b) || (c && d);
            // cout << dp[k][l] << ' ';
        }
        // cout << '\n';
    }

    cout << (dp[2][n-1] ? "YES" : "NO");
}