#include <bits/stdc++.h>

#define DIV 1000000007

using namespace std;

int main() {
    freopen("input/2.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N;
    cin >> N;
    vector<pair<int, int>> sweep;
    vector<pair<int, int>> seg;
    for(int i=0; i<N; i++) {
        int l, r;
        cin >> l >> r;
        sweep.emplace_back(l, 1);
        sweep.emplace_back(r, -1);
        seg.emplace_back(l, r);
    }

    sort(sweep.begin(), sweep.end());

    vector<int> a(2*N+1);
    int acc = 0;
    for(pair<int, int> s : sweep) {
        acc += s.second;
        a[s.first] = acc;
    }

    vector<int> p(N);
    p[0] = 1;
    for(int i=1; i<N; i++)
        p[i] = (p[i-1] * 2) % DIV;

    int sum = 0;
    for(int i=0; i<N; i++)
        sum = (sum + p[N - 1 - a[seg[i].first - 1]]) % DIV;

    cout << sum;
    return 0;
}