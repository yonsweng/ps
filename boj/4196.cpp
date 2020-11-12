#include <bits/stdc++.h>

#define MAXN 100000

using namespace std;

stack<int> st;
vector<int> adj[MAXN+1];
int dfsn[MAXN+1], dfsn_cnt;
int group[MAXN+1];
vector<vector<int>> scc;

int dfs(int here)
{
	st.push(here);
	dfsn[here] = ++dfsn_cnt;

	int min_dfsn = dfsn[here];

	for(int there : adj[here]) {
		if(group[there] != -1) continue;

		if(!dfsn[there]) {  // not visited
			min_dfsn = min(min_dfsn, dfs(there));
		} else {  // visited
			min_dfsn = min(min_dfsn, dfsn[there]);
		}
	}

	// pop stack and grouping
	if(min_dfsn == dfsn[here]) {
		vector<int> temp;
		while(!st.empty()) {
			int node = st.top();  st.pop();
			temp.push_back(node);
			group[node] = scc.size();
			if(node == here) break;
		}
		scc.push_back(temp);
	}

	return min_dfsn;
}

int main()
{
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--) {
        int n, m;
        cin >> n >> m;

        scc.clear();
        dfsn_cnt = 0;
        for(int i=1; i<=n; i++) {
            adj[i].clear();
            dfsn[i] = 0;
            group[i] = -1;
        }

        for(int i=0; i<m; i++) {
            int x, y;
            cin >> x >> y;
            adj[x].push_back(y);
        }

        for(int i=1; i<=n; i++) {
            if(!dfsn[i]) {
                dfs(i);
            }
        }

        int answer = 0;
        vector<set<int>> dag(scc.size());
        vector<bool> in(scc.size(), false);

        for(int i=int(scc.size())-1; i>=0; i--) {
            if(!in[i]) answer++;
            for(auto node : scc[i]) {
                for(auto to : adj[node]) {
                    if(group[to] == i) continue;
                    dag[i].insert(group[to]);
                    in[group[to]] = true;
                }
            }
        }

        cout << answer << '\n';

        assert(st.empty());
    }
}