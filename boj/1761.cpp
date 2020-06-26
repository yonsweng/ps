#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

#define MAXN 40000

using namespace std;

vector<pair<int, int> > adj[MAXN+1];
pair<int, int> parent[MAXN+1][17];

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	for(int i=0; i<n-1; i++) {
		int u, v, w;
		cin >> u >> v >> w;

		adj[u].push_back({v, w});
		adj[v].push_back({u, w});
	}

	// Make a tree.
	queue<int> q;
	bool inq[MAXN+1] = {};
	int depth[MAXN+1];

	q.push(1);
	inq[1] = true;
	depth[1] = 0;

	while(!q.empty()) {
		int here = q.front();
		q.pop();

		for(pair<int, int> pair_there : adj[here]) {
			int there = pair_there.first, weight = pair_there.second;
			if(!inq[there]) {
				q.push(there);
				inq[there] = true;
				depth[there] = depth[here] + 1;

				parent[there][0] = make_pair(here, weight);
			}
		}
	}

	const int MAXJ = 1 + (int)log2(n-1);

	// Fill parent.
	for(int j=1; j<=MAXJ; j++) {
		for(int i=1; i<=n; i++) {
			parent[i][j].first = parent[parent[i][j-1].first][j-1].first;
			parent[i][j].second = parent[i][j-1].second + parent[parent[i][j-1].first][j-1].second;
		}
	}

	// for(int j=0; j<=MAXJ; j++) {
	// 	for(int i=1; i<=n; i++) {
	// 		cout << parent[i][j].second << '\t';
	// 	}
	// 	cout << '\n';
	// }

	int m;
	cin >> m;

	for(int i=0; i<m; i++) {
		int u, v;
		cin >> u >> v;
		if(depth[u] < depth[v]) swap(u, v);

		int dist = 0;

		int diff = depth[u] - depth[v];
		for(int j=0; diff>0; j++) {
			if(diff % 2 == 1) {
				dist += parent[u][j].second;
				u = parent[u][j].first;
			}
			diff /= 2;
		}

		if(u != v) {
			for(int j=MAXJ; j>=0; j--) {
				if(parent[u][j].first != parent[v][j].first) {
					dist += (parent[u][j].second + parent[v][j].second);
					u = parent[u][j].first;
					v = parent[v][j].first;
				}
			}

			int lca = parent[u][0].first;
			dist += parent[u][0].second + parent[v][0].second;
		}

		cout << dist << '\n';
	}

	return 0;
}