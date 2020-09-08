#include <bits/stdc++.h>

using namespace std;

vector<int> cnt_ones(int N) {
    vector<int> cnt(1<<N);
    for(int i=0; i<(1<<N); i++) {
        for(int j=0; (1<<j)<=i; j++) {
            cnt[i] += bool(i & (1 << j));
        }
    }
    return cnt;
}

vector<int> available(int N) {
    vector<int> ret;
    for(int a=0; a<(1<<N); a++) {
        bool good = true;
        for(int i=0; i<N-1; i++) {
            if((a & (3 << i)) == (3 << i)) {
                good = false;
            }
        }
        if(good) ret.push_back(a);
    }
    return ret;
}

bool check(int a, int b) {
    if((a & (b << 1)) || (a & (b >> 1))) return false;
    return true;
}

int main() {
    // freopen("1.in", "r", stdin);

    int C;
    cin >> C;

    while(C--) {
        int M, N;
        cin >> M >> N;

        int seat[11] = {};
        for(int i=1; i<=M; i++)
            for(int j=0; j<N; j++) {
                char input;
                cin >> input;
                if(input == 'x')
                    seat[i] |= 1 << j;
            }

        int dp[11][1024] = {};
        vector<int> cnt = cnt_ones(N);
        vector<int> valid = available(N);
        for(int i=1; i<=M; i++) {
            for(int j : valid) {
                for(int k : valid) {
                    if(!(k & seat[i]) && check(j, k)) {
                        dp[i][k] = max(dp[i][k], dp[i-1][j] + cnt[k]);
                    }
                }
            }
        }
        
        int answer = 0;
        for(int j : valid) {
            answer = max(answer, dp[M][j]);
        }
        cout << answer << '\n';
    }
}