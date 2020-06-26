#include <iostream>
#include <queue>
#include <cmath>
#include <algorithm>

#define MAXN 100000

using namespace std;

vector<int> adj[MAXN+1];
int parent[MAXN+1][18];

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	for(int i=0; i<n-1; i++) {
		int u, v;
		cin >> u >> v;

		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	// Find parents of all nodes.
	queue<int> q;
	q.push(1);

	bool inq[MAXN+1] = {};
	inq[1] = true;

	int depth[MAXN+1] = {};

	while(!q.empty()) {
		int here = q.front();
		q.pop();

		for(int there : adj[here]) {
			if(inq[there] == false) {
				// cout << here << ' ' << there << '\n';
				q.push(there);
				inq[there] = true;

				parent[there][0] = here;
				depth[there] = depth[here] + 1;
			}
		}
	}

	// Fill parent array.
	for(int j=1; j<=1+log2(n-1); j++) {
		for(int i=1; i<=n; i++) {
			parent[i][j] = parent[parent[i][j-1]][j-1];
		}
	}

	// for(int j=0; j<=1+log2(n-1); j++) {
	// 	for(int i=1; i<=n; i++)
	// 		cout << parent[i][j] << '\t';
	// 	cout << '\n';
	// }

	// Queries.
	int m;
	cin >> m;

	for(int i=0; i<m; i++) {
		int u, v;
		cin >> u >> v;

		if(depth[u] < depth[v]) swap(u, v);  // depth[u] >= depth[v]

		// Make depth[u] = depth[v].
		int depth_diff = depth[u] - depth[v], cnt = 0;
		while(depth_diff > 0) {
			if(depth_diff % 2 == 1)
				u = parent[u][cnt];

			depth_diff /= 2;
			cnt++;
		}

		for(int j=1+log2(n-1); j>=0; j--) {
			if(parent[u][j] != parent[v][j]) {
				u = parent[u][j];
				v = parent[v][j];
			}
		}

		int answer = (u != v) ? parent[u][0] : u;
		cout << answer << '\n';
	}

	return 0;
}