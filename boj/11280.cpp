#include <bits/stdc++.h>

#define MAXV 20001

using namespace std;

vector<int> adj[MAXV];
int dfsn[MAXV], DFSN, sn[MAXV], SN;
bool closed[MAXV];
stack<int> st;

// Return the smallest dfsn.
int tarjan(int now)
{
	int min_dfsn = dfsn[now] = ++DFSN;
	st.push(now);

	for(int next : adj[now])
		if(dfsn[next] == 0)
			min_dfsn = min(min_dfsn, tarjan(next));
		else if(!closed[next])
			min_dfsn = min(min_dfsn, dfsn[next]);

	if(min_dfsn == dfsn[now]) {
		SN++;
		while(!st.empty()) {
			int top = st.top(); st.pop();
			sn[top] = SN;
			closed[top] = true;
			if(top == now) break;
		}
	}

	return min_dfsn;
}

// negative -> odd, positive -> even
inline int idx(int a)
{
	return (a < 0) ? (2*(-a)-1) : (2*a);
}

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int v, e;
	cin >> v >> e;

	while(e--) {
		int x, y;
		cin >> x >> y;
		adj[idx(-x)].push_back(idx(y));
		adj[idx(-y)].push_back(idx(x));
	}

	for(int i=1; i<=2*v; i++)
		if(!closed[i]) tarjan(i);

	bool ok = true;
	for(int i=1; i<=2*v; i+=2)
		if(sn[i] == sn[i+1]) {
			ok = false;
			break;
		}

	// Print out the answer.
	if(ok) cout << 1;
	else cout << 0;

	return 0;
}