#include <iostream>
#include <vector>

using namespace std;

int dp[5000][10001];

bool is_prime(int k) {
    for(int d = 2; d * d <= k; d++) {
        if(k % d == 0) {
            return false;
        }
    }
    return true;
}

void get_primes(int n, vector<int> &primes) {
    for(int k = 2; k <= n; k++) {
        if(is_prime(k)) {
            primes.push_back(k);
        }
    }
}

int main() {
    // freopen("input/1.in", "r", stdin);
    int N, M;
    cin >> N >> M;

    vector<int> p;
    get_primes(N, p);

    for(int i = 0; i < int(p.size()); i++) {
        dp[i][0] = 1;
    }
    for(int j = p[0]; j <= N; j *= p[0]) {
        dp[0][j] = j;
    }
    for(int i = 1; i < int(p.size()); i++) {
        for(int j = 1; j <= N; j++) {
            dp[i][j] = dp[i-1][j];
            for(int pi_l = p[i]; j - pi_l >= 0; pi_l *= p[i]) {
                dp[i][j] = ((long long)dp[i - 1][j - pi_l] * pi_l % M + dp[i][j]) % M;
            }
        }
    }

    for(int i = 0; i < int(p.size()); i++) {
        for(int j = 1; j <= N; j++) {
            cout << dp[i][j] << '\t';
        }
        cout << '\n';
    }

    int sum = 1;
    for(int j = 1; j <= N; j++) {
        sum = (sum + dp[int(p.size()) - 1][j]) % M;
    }
    cout << sum;

    return 0;
}