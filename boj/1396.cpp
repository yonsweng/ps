#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, w;

    Edge(int u, int v, int w) : u(u), v(v), w(w) {}

    bool operator<(const Edge &a) const {
        return w < a.w;
    }
};

int n;
int node_num;
int parent[200000];
int par[200000][21];
pair<int, int> node_info[200000];  // size, weight
vector<Edge> edges;
vector<int> vt[200000];
bool visited[200000];
int d[200000];

int my_find(int u) {
    if (parent[u] <= 0) return u;
    return parent[u] = my_find(parent[u]);
}

void my_union(int pu, int pv, int w) {
    ++node_num;
    parent[pu] = node_num;
    parent[pv] = node_num;
    node_info[node_num].first = node_info[pu].first + node_info[pv].first;
    node_info[node_num].second = w;
    vt[pu].push_back(node_num);
    vt[node_num].push_back(pu);
    vt[pv].push_back(node_num);
    vt[node_num].push_back(pv);
}

void kruskal() {
    sort(edges.begin(), edges.end());

    for (Edge edge : edges) {
        int u = edge.u, v = edge.v, w = edge.w;
        int pu = my_find(u), pv = my_find(v);
        if (pu != pv)
            my_union(pu, pv, w);
    }
}

void dfs(int here, int depth) {
    visited[here] = true;
    d[here] = depth;
    for (auto there : vt[here]) {
        if (visited[there])
            continue;
        par[there][0] = here;
        dfs(there, depth + 1);
    }
}

void f() {
    for (int j = 1; j < 21; j++) {
        for (int i = 1; i < 2 * n; i++) {
            par[i][j] = par[par[i][j - 1]][j - 1];
        }
    }
}

bool lca(int x, int y, int &c, int &v) {
    if (d[x] > d[y])
        swap(x, y);
    for (int i = 20; i >= 0; i--) {
        if (d[y] - d[x] >= (1 << i)) {
            y = par[y][i];
        }
    }
    if (x != y) {
        for (int i = 20; i >= 0; i--) {
            if (par[x][i] != par[y][i]) {
                x = par[x][i];
                y = par[y][i];
            }
        }
    }

    x = (par[x][0] != 0) ? par[x][0] : x;
    y = (par[y][0] != 0) ? par[y][0] : y;

    if(x != y) return false;

    c = node_info[x].second;
    v = node_info[x].first;

    return true;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int m;
    cin >> n >> m;
    node_num = n;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges.emplace_back(a, b, c);
    }

    for(int i = 1; i <= n; i++) node_info[i].first = 1;

    kruskal();

    for (int i = 1; i < 2 * n; i++) {
        if (!parent[i]) dfs(i, 0);
    }

    f();

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; i++) {
        int x, y;
        cin >> x >> y;

        int c, v;
        if (lca(x, y, c, v)) cout << c << ' ' << v << '\n';
        else cout << "-1\n";
    }

    return 0;
}
