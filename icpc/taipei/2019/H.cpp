#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    while (T--) {
        // PROOF BY AC
        long long N;
        cin >> N;
        cout << ((N * (N + 1)) ^ (N + 1)) << '\n';
    }
}