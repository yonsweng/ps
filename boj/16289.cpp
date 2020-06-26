#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>

#define MAXN 100000

using namespace std;

vector<int> adj[MAXN+1];
int parent[MAXN+1][18];

int main()
{
	//freopen("1.in", "r", stdin);
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

	int sigma[MAXN+1];
	for(int i=1; i<=n; i++)
		cin >> sigma[i];

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

		for(int there : adj[here])
			if(!inq[there]) {
				q.push(there);
				inq[there] = true;
				depth[there] = depth[here] + 1;

				parent[there][0] = here;
			}
	}

	// Fill up the parent array.
	for(int j=1; j<=1+log2(n-1); j++)
		for(int i=1; i<=n; i++)
			parent[i][j] = parent[parent[i][j-1]][j-1];

	int answer = 0;

	// Find LCAs.
	for(int s=1; s<=n-1; s++) {
		int u = sigma[s], v = sigma[s+1];
		int du = depth[u], dv = depth[v];
		if(du < dv) swap(u, v);  // Ensure depth[u] >= depth[v].

		// Make depth[u] = depth[v].
		int depth_diff = depth[u] - depth[v], cnt = 0;
		while(depth_diff > 0) {
			if(depth_diff % 2 == 1) u = parent[u][cnt];
			cnt++;
			depth_diff /= 2;
		}

		// Find the LCA of u and v.
		for(int j=1+log2(n-1); j>=0; j--)
			if(parent[u][j] != parent[v][j]) {
				u = parent[u][j];
				v = parent[v][j];
			}

		int lca = (u == v) ? u : parent[u][0];
		int path_len = du + dv - 2 * depth[lca];

		answer = max(answer, path_len);
	}

	cout << (answer > 3 ? 99 : answer);

	return 0;
}