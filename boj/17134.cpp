#include <iostream>
#include <complex>
#include <vector>

#define MAXN 1000000

using namespace std;
using cpx = complex<double>;

void fft(vector<cpx> &f, bool inv=false) {
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

void multiply(vector<cpx> &a, vector<cpx> &b) {
    const int N = a.size();
    int n;
    for (n = 1; n < 2 * N; n *= 2);
    a.resize(n), b.resize(n);
    for (int i = 0; i < N; i++)
        b[n - N + i] = b[i];
    fft(a), fft(b);
    for (int i = 0; i < n; i++)
        a[i] *= b[i];
    fft(a, true);
    a.resize(N);
}

void get_polynomials(vector<cpx> &a, vector<cpx> &b) {
    // get primes below 1000
    vector<int> primes;
    for(int n = 2; n * n <= MAXN; n++) {
        bool is_prime = true;
        for(int d = 2; d * d <= n; d++) {
            if(n % d == 0) {
                is_prime = false;
                break;
            }
        }
        if(is_prime)
            primes.push_back(n);
    }

    // elimination
    a[0] = a[1] = a[2] = cpx(0., 0.);
    for(int p : primes) {
        for(int k = 2 * p; k <= MAXN; k += p) {
            a[k] = cpx(0., 0.);
        }
    }

    b[4] = cpx(1., 0.);
    for(int k = 6; k <= MAXN; k += 2)
        b[k] = a[k / 2];

    // compression
    // int N = MAXN / 2;
    // int i;
    // for(i = 0; 2 * i + 3 <= MAXN; i++)
    //     a[i] = a[2 * i + 3];
    // for( ; i < N; i++)
    //     a[i] = cpx(0., 0.);
    // a.resize(N);

    // for(i = 0; 2 * i + 4 <= MAXN; i++)
    //     b[i] = b[2 * i + 4];
    // for( ; i < N; i++)
    //     b[i] = cpx(0., 0.);
    // b.resize(N);
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);
    vector<cpx> a(MAXN + 1, {1., 0.}), b(MAXN + 1, {0., 0.});  // a: prime, b: 2*prime
    get_polynomials(a, b);
    multiply(a, b);

    vector<int> c(MAXN + 1);
    // for(int i = 0; 2 * i + 7 <= MAXN; i++)
    //     c[2 * i + 7] = int(round(a[i].real())) + int(round(b[i].real()));

    int T; cin >> T;
    while(T--) {
        int N; cin >> N;
        cout << int(round(a[N].real())) << '\n';
    }
}