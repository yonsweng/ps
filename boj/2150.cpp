#include <bits/stdc++.h>

#define MAXV 10001

using namespace std;

int v, dfsn[MAXV], cnt;
bool closed[MAXV];
vector<int> adj[MAXV];
vector<vector<int> > scc;
stack<int> nodes;

// Return the minimum dfsn of anscestors.
int tarjanSCC(int i)
{
	dfsn[i] = ++cnt;
	nodes.push(i);

	int min_anscestor = dfsn[i];

	for(int j : adj[i]) {
		if(!closed[j]) {
			if(dfsn[j]) min_anscestor = min(min_anscestor, dfsn[j]);
			else min_anscestor = min(min_anscestor, tarjanSCC(j));
		}
	}

	if(min_anscestor == dfsn[i]) {
		vector<int> vertexes;
		while(!nodes.empty()) {
			int top = nodes.top();
			nodes.pop();
			vertexes.push_back(top);
			closed[top] = true;
			if(top == i) break;
		}
		sort(vertexes.begin(), vertexes.end());
		scc.push_back(vertexes);
	}

	return min_anscestor;
}

int main()
{
	freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int e;
	cin >> v >> e;

	while(e--) {
		int from, to;
		cin >> from >> to;
		adj[from].push_back(to);
	}

	for(int i=1; i<=v; i++) {
		if(!closed[i]) tarjanSCC(i);
	}

	// Print out the answer.
	cout << scc.size();
	sort(scc.begin(), scc.end());
	for(vector<int> vertexes : scc) {
		cout << '\n';
		for(int vertex : vertexes)
			cout << vertex << ' ';
		cout << -1;
	}

	return 0;
}