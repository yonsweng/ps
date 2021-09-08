#include <iostream>

#define P 998244353

using namespace std;
using ll = long long;

long long modFact(long long n, long long p)
{
    if (n >= p)
        return 0;

    long long result = 1;
    for (int i = 1; i <= n; i++)
        result = (result * i) % p;

    return result;
}

ll fact[3000005],factInv[3000005];

ll mpow(ll x,ll m) {
    if(!m) return 1;
    ll tmp = mpow(x,m/2);
    tmp = tmp*tmp % P;
    if(m % 2) return tmp*x%P;
    return tmp;
}

ll Com(ll x,ll r) {
    return fact[x]*factInv[r]%P*factInv[x-r]%P;
}

int a[200000];

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    fact[0] = 1;
    for(int i = 1;i <= 3000000;i++) fact[i] = fact[i-1]*i%P;
    factInv[3000000] = mpow(fact[3000000],P-2);
    for(int i = 2999999;i >= 0;i--) factInv[i] = factInv[i+1]*(i+1)%P;

    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        int maxa = 0;
        for(int i=0; i<n; i++) {
            cin >> a[i];
            if(maxa < a[i])
                maxa = a[i];
        }

        int max_cnt = 0;
        for(int i=0; i<n; i++) {
            if(maxa == a[i])
                max_cnt += 1;
        }

        int answer;
        if(max_cnt >= 2) {
            answer = modFact(n, P);
        } else {
            int secmax = 0;
            for(int i=0; i<n; i++) {
                if(maxa > a[i] && secmax < a[i])
                    secmax = a[i];
            }
            int n_secmax = 0;
            for(int i=0; i<n; i++) {
                if(secmax == a[i])
                    n_secmax += 1;
            }

            if(secmax + 2 <= maxa) {
                answer = 0;
            }
            // else if(n_secmax == 1) {
            //     answer = modFact(n-1, P);
            // }
            else {
                // cout << "n_secmax: " << n_secmax << '\n';
                answer = ((long long)modFact(n_secmax, P) * (long long)n_secmax % P) * modFact(n-n_secmax-1, P) % P * Com(n, n_secmax+1) % P;
            }
        }

        cout << answer << '\n';
    }
}