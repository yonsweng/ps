#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

vector<set<int>> adj;
vector<bool> visited;
vector<int> leaves;
vector<pair<int, int>> ans;

bool isCycle(int prev, int curr) {
    bool cycle = false;
    visited[curr] = true;
    if(adj[curr].size() == 1) {  // curr is leaf
        leaves.push_back(curr);
    }
    for(int next : adj[curr]) {
        if(next != prev) {
            if(visited[next]) {
                cycle = true;
            } else {
                if(isCycle(curr, next)) {
                    cycle = true;
                }
            }
        }
    }
    return cycle;
}

void removeLeaves() {
    for(int i=0; i<leaves.size(); i++) {
        int leaf = leaves[i];
        int next = *adj[leaf].begin();
        adj[next].erase(leaf);
        if(adj[next].size() == 1) {
            leaves.push_back(next);
        }
    }
    for(int leaf : leaves) {
        int next = *adj[leaf].begin();
        if(adj[next].size() > 1) {
            ans.emplace_back(next, leaf);
        }
    }
}

void putSignsOnLeaves() {
    for(int leaf : leaves) {
        int next = *adj[leaf].begin();
        ans.emplace_back(leaf, next);
    }
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    adj.resize(n+1);
    visited.resize(n+1);

    for(int i=0; i<m; i++) {
        int v, w;
        cin >> v >> w;
        adj[v].insert(w);
        adj[w].insert(v);
    }

    for(int i=1; i<=n; i++) {
        if(!visited[i]) {
            if(isCycle(0, i)) {  // not tree
                removeLeaves();
            } else {  // tree
                putSignsOnLeaves();
            }
            leaves.clear();
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for(pair<int, int> vw : ans) {
        cout << vw.first << ' ' << vw.second << '\n';
    }

    return 0;
}