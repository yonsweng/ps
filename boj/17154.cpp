#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

vector<vector<int>> adj;
bool visited[500001], visited2[500001];
bool in_cycle[500001];
vector<pair<int, int>> ans;
stack<int> st;
bool in_st[500001];

int search_cycle(int now, int prev) {
    
}

// return now is in cycle
bool put_sign_on_cycle(int now, int prev) {
    bool is_cycle = false;
    visited2[now] = true;
    for(int to : adj[now]) {
        if(to == prev) continue;

        if(visited2[to]) {
            is_cycle = true;
        } else {
            if(put_sign_on_cycle(to, now)) {
                is_cycle = true;
            } else if(in_cycle[now]) {
                ans.emplace_back(now, to);
            }
        }
    }
    return is_cycle;
}

void put_sign_on_leaf(int now, int prev) {
    visited2[now] = true;
    if(adj[now].size() == 1) {  // leaf
        ans.emplace_back(now, adj[now][0]);
        if(!visited2[adj[now][0]])
            put_sign_on_leaf(adj[now][0], now);
    } else {
        for(int to : adj[now]) {
            if(to == prev) continue;

            if(!visited2[to])
                put_sign_on_leaf(to, now);
        }
    }
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    adj.resize(n+1);
    for(int i=0; i<m; i++) {
        int v, w;
        cin >> v >> w;
        adj[v].push_back(w);
        adj[w].push_back(v);
    }

    for(int i=1; i<=n; i++) {
        if(visited[i]) continue;

        while(!st.empty()) st.pop();

        // search cycle
        int cycle = search_cycle(i, 0);

        if(cycle) {
            // start in cycle
            put_sign_on_cycle(cycle, 0);
        } else {
            put_sign_on_leaf(i, 0);
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for(pair<int, int> vw : ans) {
        cout << vw.first << ' ' << vw.second << '\n';
    }

    return 0;
}