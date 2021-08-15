#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

#define MAXN 2000

using namespace std;

stack<int> st;
vector<int> adj[2*MAXN+1];
int dfsn[2*MAXN+1], dfsn_cnt = 0;
vector<vector<int> > scc;
int group[2*MAXN+1];
vector<vector<int> > scc_graph;
bool visited[2*MAXN+1];

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

bool find2(int start_group) {
	visited[start_group] = true;

	if(start_group == group[2]) return true;

	for(int dest_group : scc_graph[start_group]) {
		if(!visited[dest_group]) {
			if(find2(dest_group)) return true;
		}
	}

	return false;
}

int main()
{
	while(1) {
		if(cin.eof()) {
            break;
        }

        int n, m;
        cin >> n >> m;

        if(cin.eof()) {
            break;
        }

		for(int i=1; i<=2*n; i++) adj[i].clear();
		fill_n(dfsn, 2*n+1, 0);
		dfsn_cnt = 0;
		scc.clear();
		fill_n(group, 2*n+1, -1);
		scc_graph.clear();
		fill_n(visited, 2*n+1, false);

		for(int i=0; i<m; i++) {
			int a, b;
			cin >> a >> b;

			if(a < 0) a = (-a) * 2;
			else a = a * 2 - 1;

			if(b < 0) b = (-b) * 2;
			else b = b * 2 - 1;

			int not_a = a % 2 == 0 ? (a - 1) : (a + 1);
			int not_b = b % 2 == 0 ? (b - 1) : (b + 1);

			adj[not_a].push_back(b);
			adj[not_b].push_back(a);
		}

		for(int i=1; i<=2*n; i++) {
			if(!dfsn[i]) dfs(i);
		}

		// for debugging
		for(int i=1; i<=2*n; i++) {
			cout << group[i] << ' ';
		}
		cout << '\n';

		// If a and not_a are in the same component, then print no.
		bool no = false;

		// If we can go 1->2, then print no.
		// Make a scc graph.
		scc_graph.resize(scc.size());
		for(int i=1; i<=2*n; i++) {
			for(int j : adj[i]) {
				scc_graph[group[i]].push_back(group[j]);
			}
		}

		if(find2(group[1])) {
			no = true;
		}
		else {
			for(int i=1; i<=2*n; i+=2) {
				if(group[i] == group[i+1]) {
					no = true;
					break;
				}
			}
		}
		if(no) cout << "no\n";
		else cout << "yes\n";
	}
}