#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> adj[100001];
bool no[4][100001];
int group[100001];

void dfs(int j)
{
	if(j > n) {
		bool check[4] = {};
		for(int i=1; i<=n; i++) {
			check[group[i]] = true;
		}

		if(check[1] && check[2] && check[3]) {
			for(int i=1; i<=n; i++) {
				cout << group[i] << ' ';
			}
			exit(0);
		}

		else {
			cout << -1;
			exit(0);
		}
	}

	for(int i=1; i<=3; i++) {
		if(no[i][j] == false) {
			bool flag = false;
			for(int k : adj[j]) {
				if(group[k] == i) {
					flag = true;
					break;
				}
			}
			if(flag) break;

			for(int k : adj[j]) {
				no[i][k] = true;
			}

			group[j] = i;
			dfs(j+1);

			for(int k : adj[j]) {
				no[i][k] = false;
			}

			break;
		}
	}
}

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int m;
	cin >> n >> m;

	while(m--) {
		int u, v;
		cin >> u >> v;

		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	dfs(1);

	cout << -1;

	return 0;
}