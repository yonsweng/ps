// BOJ 2644 촌수계산 https://www.acmicpc.net/problem/2644
#include <iostream>
#include <vector>

#define MAXN 101
#define MAX_PSIZE 7

using namespace std;

int n, p[MAXN][MAX_PSIZE], d[MAXN];
vector<int> adj[MAXN];
bool v[MAXN];

void dfs(int i, int depth) {
    v[i] = true, d[i] = depth;
    for (int j : adj[i])
        if (!v[j]) dfs(j, depth + 1);
}

void compute_p() {
    for (int j = 1; j < MAX_PSIZE; j++)
        for (int i = 1; i <= n; i++)
            p[i][j] = p[p[i][j - 1]][j - 1];
}

int find_lca(int a, int b) {
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

    int a, b, m, lca;
    cin >> n;
    cin >> a >> b;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int x, y;  // x: parent, y: child
        cin >> x >> y;
        adj[x].push_back(y), adj[y].push_back(x);
        p[y][0] = x;
    }

    for (int i = 1; i <= n; i++)
        if (!p[i][0]) dfs(i, 0);

    compute_p();
    lca = find_lca(a, b);

    if (lca != -1) cout << d[a] + d[b] - 2 * d[lca];
    else cout << -1;

    return 0;
}