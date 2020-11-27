#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1000, INF = 200000001;
int N, K, v[MAXN];
vector<int> a[MAXN];
map<int, int> d[MAXN][2];  // (n, v)

void insert(map<int, int> &m, int key, int value) {
    if (m.find(key) != m.end())
        m[key] = max(m[key], value);
    else
        m[key] = value;
}

void tree_dp(int i) {
    d[i][1][1] = v[i];
    for (int c : a[i]) {
        tree_dp(c);

        map<int, int> tmp0;
        for (auto dc : d[c][0])
            insert(tmp0, dc.first, dc.second);
        for (auto dc : d[c][1])
            insert(tmp0, dc.first, dc.second);
        for (auto di : d[i][0]) {
            for (auto dc : d[c][0])
                if (di.first + dc.first <= K)
                    insert(tmp0, di.first + dc.first, di.second + dc.second);
                else
                    break;
            for (auto dc : d[c][1])
                if (di.first + dc.first <= K)
                    insert(tmp0, di.first + dc.first, di.second + dc.second);
                else
                    break;
        }
        for (auto kv : tmp0)
            insert(d[i][0], kv.first, kv.second);

        map<int, int> tmp1;
        for (auto di : d[i][1])
            for (auto dc : d[c][0])
                if (di.first + dc.first <= K)
                    insert(tmp1, di.first + dc.first, di.second + dc.second);
                else
                    break;
        for (auto kv : tmp1)
            insert(d[i][1], kv.first, kv.second);
    }
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        cin >> N >> K;
        for (int i = 0; i < N; i++) {
            cin >> v[i];
            a[i].clear();
            d[i][0].clear();
            d[i][1].clear();
        }
        for (int i = 1; i < N; i++) {
            int p;
            cin >> p;
            a[p].push_back(i);
        }
        tree_dp(0);
        int answer = -INF;
        for (auto kv : d[0][0])
            answer = max(answer, kv.second);
        for (auto kv : d[0][1])
            answer = max(answer, kv.second);
        cout << answer << '\n';
    }
}