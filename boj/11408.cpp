#include <bits/stdc++.h>
#define INF 987654321

using namespace std;

struct Edge {
    int v, cap, cost, rev;
    Edge(int v, int cap, int cost, int rev) : v(v), cap(cap), cost(cost), rev(rev) {}
};

vector<vector<Edge>> vt;

void add_edge(int s, int e, int c, int w) {
    vt[s].emplace_back(e, c, w, (int)vt[e].size());
    vt[e].emplace_back(s, 0, 0, (int)vt[s].size() - 1);
}

int main() {
    int n, m;
    cin >> n >> m;

    vt.resize(n+m+2);

    // employees -> works
    for(int i=1; i<=n; i++) {
        int cnt;
        cin >> cnt;
        while(cnt-- > 0) {
            int work, wage;
            cin >> work >> wage;
            add_edge(i, n+work, 1, wage);
        }
    }

    // src -> employees
    int src = 0;
    for(int i=1; i<=n; i++) {
        add_edge(src, i, 1, 0);
    }

    // works -> sink
    int sink = n+m+1;
    for(int i=n+1; i<=n+m; i++) {
        add_edge(i, sink, 1, 0);
    }

    int result = 0;
    int cnt = 0;
 
    while (1) {
        vector<int> dist(n+m+2, INF);
        vector<pair<int, int>> prev(n+m+2, {-1, -1});
        vector<bool> inQ(n+m+2, false);

        // SPFA
        dist[src] = 0;
        queue<int> q;
        q.push(src);
        inQ[src] = true;
        while (!q.empty()) {
            int here = q.front();
            q.pop();
            inQ[here] = false;
            for(int i=0; i<vt[here].size(); i++) {
                int next = vt[here][i].v;
                if (vt[here][i].cap > 0 && dist[next] > dist[here] + vt[here][i].cost) {
                    dist[next] = dist[here] + vt[here][i].cost;
                    prev[next] = make_pair(here, i);
                    if (!inQ[next]) {
                        q.push(next);
                        inQ[next] = true;
                    }
                }
            }
        }
 
        if (prev[sink].first == -1)
            break;
 
        // 최대 유량
        int flow = INF;
        for (int i = sink; i != src; i = prev[i].first)
            flow = min(flow, vt[prev[i].first][prev[i].second].cap);

        for (int i = sink; i != src; i = prev[i].first) {
            result += vt[prev[i].first][prev[i].second].cost;
            vt[i][vt[prev[i].first][prev[i].second].rev].cost -= vt[prev[i].first][prev[i].second].cost;
            vt[prev[i].first][prev[i].second].cost = 0;
            vt[prev[i].first][prev[i].second].cap -= flow;
            vt[i][vt[prev[i].first][prev[i].second].rev].cap += flow;
        }
 
        cnt += flow;
    }

    cout << cnt << '\n' << result;
}