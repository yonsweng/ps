#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        int N, K, S;
        cin >> N >> K >> S;

        long long restart = (K - 1) + 1 + N;
        long long back = (long long)(K - 1) + (K - S) + (N - S + 1);

        cout << "Case #" << x << ": " << min(restart, back) << '\n';
    }

    return 0;
}