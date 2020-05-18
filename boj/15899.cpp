#include <iostream>
#include <vector>
#include <algorithm>

#define MAXN 200000

using namespace std;

int N, M, C;
int color[MAXN+1];
vector<int> adj[MAXN+1];
int cnt;
int in[MAXN+1], out[MAXN+1];
int cl[MAXN+1];
vector<int> tree[4*MAXN+1];

void dfs(int i) {
    in[i] = ++cnt;
    cl[cnt] = color[i];
    for(int j : adj[i]) if(!in[j]) dfs(j);
    out[i] = cnt;
}

void update(int ti, int s, int e, int x) {
    if(x < s || e < x) return;
    tree[ti].push_back(cl[x]);
    if(s != e) {
        int mid = (s + e) / 2;
        update(ti*2, s, mid, x);
        update(ti*2+1, mid+1, e, x);
    }
}

int get_sum(int ti, int s, int e, int x, int y, int c) {
    if(e < x || y < s) return 0;
    if(x <= s && e <= y)
        return upper_bound(tree[ti].begin(), tree[ti].end(), c) - tree[ti].begin();
    int mid = (s + e) / 2;
    return get_sum(ti*2, s, mid, x, y, c) + get_sum(ti*2+1, mid+1, e, x, y, c);
}

int main() {
    cin >> N >> M >> C;
    for(int i=1; i<=N; i++) {
        cin >> color[i];
    }
    for(int i=1; i<=N-1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1);

    for(int i=1; i<=N; i++) update(1, 1, N, i);

    for(int i=1; i<=4*N; i++) sort(tree[i].begin(), tree[i].end());

    int ans = 0;
    for(int i=1; i<=M; i++) {
        int v, c;
        cin >> v >> c;
        ans = (ans + get_sum(1, 1, N, in[v], out[v], c)) % 1000000007;
    }
    cout << ans;

    // debug
    // cout << '\n';
    // for(int a : tree[1]) cout << a << ' ';
    return 0;
}