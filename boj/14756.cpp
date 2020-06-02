#include <iostream>
#include <algorithm>
#include <complex>
#include <vector>

using namespace std;
using cpx = complex<double>;
const double PI = acos(-1);

inline unsigned int bit_reverse(const unsigned int n, const unsigned int k) {
    unsigned int r, i;
    for (r = 0, i = 0; i < k; ++i)
        r |= ((n >> i) & 1) << (k - i - 1);
    return r;
}

void fft(vector<cpx>& f, bool inv=false)
{
    int n = f.size();
    vector<cpx> g = f;

    for (int i = 0; i < n; ++i)
    {
        int sz = n, shift = 0, idx = i;
        while (sz > 1)
        {
            if (idx & 1)
                shift += sz >> 1;
            idx >>= 1;
            sz >>= 1;
        }
        f[shift + idx] = g[i];
    }

    for (int i = 1; i < n; i <<= 1)
    {
        double x = inv ? PI / i : -PI / i;
        cpx w = {cos(x), sin(x)};

        for (int j = 0; j < n; j += i << 1)
        {
            cpx th = {1, 0};
            for (int k = 0; k < i; ++k)
            {
                cpx tmp = f[i + j + k] * th;
                f[i + j + k] = f[j + k] - tmp;
                f[j + k] += tmp;
                th *= w;
            }
        }
    }

    if (inv)
    {
        for (int i = 0; i < n; ++i)
        {
            f[i] /= n;
        }
    }
}

// c[k] = a[0]*b[k] + a[1]*b[k-1] + ... + a[k]*b[0]
// 
void GetConvolution(vector<cpx>& a, vector<cpx>& b)
{
    int N = a.size();
    int n = 1;
    while (n <= a.size() || n <= b.size())
        n *= 2;
    
    a.resize(n);
    b.resize(n);
    cpx w(cos(2 * PI/n), sin(2 * PI/n));

    fft(a, false);
    fft(b, false);

    for (int i = 0; i < n; ++i)
        a[i] = a[i] * b[i];

    fft(a, true);
    for (int i = 0; i < n; ++i)
        a[i] = cpx(a[i].real(), a[i].imag());

    a.resize(N);
}


int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    vector<cpx> T[100], P[100];

    int n, l, m;
    long long W;
    cin >> n >> l >> m >> W;

    for(int i=0; i<m; i++) {
        T[i].reserve(n);
        P[i].reserve(l);
    }

    for(int i=0; i<m; i++)
        for(int j=0; j<n; j++) {
            int tmp;
            cin >> tmp;
            T[i].push_back(tmp);  // sky
        }
    for(int i=0; i<m; i++) {
        for(int j=0; j<l; j++) {
            int tmp;
            cin >> tmp;
            P[i].push_back(tmp);  // telescope
        }
    }

    for(int i=0; i<m; i++)
        reverse(P[i].begin(), P[i].end());  // reverse telescope

    for(int i=0; i<m; i++)
        GetConvolution(T[i], P[i]);  // T[i] = T[]

    int cnt = 0;
    for(int j=l-1; j<n; j++) {
        double sum = 0;
        for(int i=0; i<m; i++)
            sum += T[i][j].real();
        if((long long)round(sum) > W) cnt++;
    }
    cout << cnt;
    
    return 0;
}