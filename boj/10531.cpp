#include <iostream>
#include <complex>
#include <vector>
#include <cmath>

using namespace std;

typedef complex<double> cpx;
typedef vector<cpx> vec;

void DFT(vector<cpx> &f, bool inv = false) {
    int n = f.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int b = n >> 1;
        while (!((j ^= b) & b)) b >>= 1;
        if (i < j) swap(f[i], f[j]);
    }
    for (int k = 1; k < n; k <<= 1) {
        double a = (inv ? M_PI / k : -M_PI / k);
        cpx w(cos(a), sin(a));
        for (int i = 0; i < n; i += (k << 1)) {
            cpx wp(1, 0);
            for (int j = 0; j < k; ++j) {
                cpx x = f[i + j], y = f[i + j + k] * wp;
                f[i + j] = x + y;
                f[i + j + k] = x - y;
                wp *= w;
            }
        }
    }
    if (inv)
        for (int i = 0; i < n; ++i) f[i] /= n;
}

void mul(vec &p) {
    int n = 1;
    while (n <= p.size()) n <<= 1;
    n <<= 1;
    p.resize(n);
    DFT(p);
    for (int i = 0; i < n; i++) p[i] = p[i] * p[i];
    DFT(p, 1);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    vector<cpx> v(202020);
    cin >> n;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        v[t] = cpx(1, 0);
    }
    v[0] = cpx(1, 0);
    mul(v);
    cin >> m;
    int ans = 0;
    for (int i = 0; i < m; i++) {
        int t;
        cin >> t;
        if (round(v[t].real()) > 0) ans++;
    }
    cout << ans;
    return 0;
}