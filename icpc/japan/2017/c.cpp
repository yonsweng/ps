#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    long long n, t;
    cin >> n >> t;
    long long a = 0, b = -1;
    for (int i = 0; i < n; i++) {
        long long h;
        cin >> h;
        a += h;
        if (b < h) {
            b = h;
            if (t < a) cout << 1 << '\n';
            else cout << (t - a) / b + 2 << '\n';
        } else {
            if (t < a) cout << 1 << '\n';
            else cout << (t - a) / b + 2 << '\n';
        }
    }
}