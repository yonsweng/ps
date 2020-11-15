#include <bits/stdc++.h>

using namespace std;
using ll = long long;

bool is_boring(ll a) {
    ll d;
    for(d = 1e18; d >= 1; d /= 10) {
        if(a / d > 0) {
            break;
        }
    }

    for(ll d_odd = d; d_odd >= 1; d_odd /= 100) {
        if(a / d_odd % 10 % 2 == 0) {
            return false;
        }
    }

    for(ll d_even = d / 10; d_even >= 1; d_even /= 100) {
        if(a / d_even % 10 % 2 == 1) {
            return false;
        }
    }

    return true;
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        ll y = 0;

        ll L, R;
        cin >> L >> R;

        ll add, p5 = 1;
        for (add = 1;; add *= 10, p5 *= 5) {
            for(; L / add % 10 != 0; L += add) {
                if(L + add > R) {
                    break;
                }
                if(is_boring(L / add)) {
                    y += p5;
                }
            }
            if(L + add > R) {
                break;
            }
        }

        for(; add >= 1; add /= 10, p5 /= 5) {
            for(; L / add % 10 != R / add % 10; L += add) {
                if(is_boring(L / add)) {
                    y += p5;
                }
            }
        }

        if(is_boring(R)) {
            y++;
        }

        cout << "Case #" << x << ": " << y << '\n';
    }

    return 0;
}