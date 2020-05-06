#include <complex>
#include <vector>

using namespace std;
using cpx = complex<double>;
const double PI = acos(-1);

inline unsigned int bitreverse(const unsigned int n, const unsigned int k) {
    unsigned int r, i;
    for (r = 0, i = 0; i < k; ++i)
        r |= ((n >> i) & 1) << (k - i - 1);
    return r;
}

void fft(vector<cpx> &a, bool is_reverse = false) {
    const unsigned int n = a.size(), k = __builtin_ctz(n);
    unsigned int s, i, j;
    for (i = 0; i < n; i++) {
        j = bitreverse(i, k);
        if (i < j)
            swap(a[i], a[j]);
    }
    for (s = 2; s <= n; s *= 2) {
        double t = 2 * PI / s * (is_reverse ? -1 : 1);
        cpx ws(cos(t), sin(t));
        for (i = 0; i < n; i += s) {
            cpx w(1);
            for (j = 0; j < s / 2; j++) {
                cpx tmp = a[i + j + s / 2] * w;
                a[i + j + s / 2] = a[i + j] - tmp;
                a[i + j] += tmp;
                w *= ws;
            }
        }
    }
    if (is_reverse)
        for (i = 0; i < n; i++)
            a[i] /= n;
}

void convolution(vector<cpx> &a, vector<cpx> &b) {
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