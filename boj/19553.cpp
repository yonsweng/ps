#include <bits/stdc++.h>

using namespace std;

int N;
int d[1001][1001][100];
vector<int> p;

int dp(int i, int j, int l, int sum) {
    i = (i + N - 1) % N + 1;
    j = (j + N - 1) % N + 1;

    if(d[i][j][l] != -1) {
        return d[i][j][l];
    }

    if(i == j) {
        return d[i][j][l] = sum;
    }

    int M = 0;

    if(l - p[i] >= 0) {
        int val = p[i] + dp(i-1, j, l-p[i], sum-p[i]);
        M = max(M, val);
    } else {
        int val = sum - dp(i-1, j, p[i]-l-1, sum-p[i]);
        M = max(M, val);
    }

    if(l - p[j] >= 0) {
        int val = p[j] + dp(i, j+1, l-p[j], sum-p[j]);
        M = max(M, val);
    } else {
        int val = sum - dp(i, j+1, p[j]-l-1, sum-p[j]);
        M = max(M, val);
    }

    return d[i][j][l] = M;
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    cin >> N;

    int sum = 0;
    p.resize(N+1);
    for(int i=1; i<=N; i++) {
        cin >> p[i];
        sum += p[i];
    }

    memset(d, -1, sizeof(int)*1001*1001*100);

    int M = 0;
    for(int i=1; i<=N; i++) {
        M = max(M, sum - dp(i-1, i+1, p[i]-1, sum-p[i]));
    }
    cout << M;

    return 0;
}