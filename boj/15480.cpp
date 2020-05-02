#include <iostream>
#include <vector>

#define MAXN 100001
#define MAX_PSIZE 17

using namespace std;

int n, p[MAXN][MAX_PSIZE], d[MAXN];
vector<int> adj[MAXN];
bool v[MAXN];

void dfs(int i, int depth) {
    v[i] = true, d[i] = depth;
    for (int j : adj[i])
        if (!v[j]) {
            p[j][0] = i;
            dfs(j, depth + 1);
        }
}

void compute_p() {
    for (int j = 1; j < MAX_PSIZE; j++)
        for (int i = 1; i <= n; i++)
            p[i][j] = p[p[i][j - 1]][j - 1];
}

int lca(int a, int b) {
    // Make a have a higher depth
    if (d[a] < d[b]) swap(a, b);

    // Elevate a to the depth of b
    int depth_diff = d[a] - d[b];
    for (int j = MAX_PSIZE - 1; j >= 0; j--)
        if (depth_diff & (1 << j))
            a = p[a][j];

    if (a == b) return a;

    for (int j = MAX_PSIZE - 1; j >= 0; j--)
        if (p[a][j] != p[b][j])
            a = p[a][j], b = p[b][j];

    if (p[a][0] == p[b][0] && p[a][0]) return p[a][0];
    else return -1;
}

int main() {
//    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y), adj[y].push_back(x);
    }

    for (int i = 1; i <= n; i++)
        if (!v[i]) dfs(i, 0);

    compute_p();

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int r, u, v;
        cin >> r >> u >> v;

        int ru = lca(r, u), rv = lca(r, v), uv = lca(u, v);
        int ans;
        if (ru == rv)
            ans = uv;
        else if(rv == uv)
            ans = ru;
        else if(uv == ru)
            ans = rv;
        else if(ru == u)
            ans = u;
        else
            ans = v;

        cout << ans << '\n';
    }

    return 0;
}