#include <bits/stdc++.h>

#define MAXV 10001

using namespace std;

int dfsn[MAXV], cnt;
bool closed[MAXV];
vector<int> adj[MAXV];
vector<vector<int> > scc;
stack<int> nodes;

// Return the minimum dfsn of anscestors.
int tarjanSCC(int i) {
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

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

    int k, n;
    cin >> k >> n;
    for(int i=1; i<=n; i++) {
        int l1, l2, l3;
        char c1, c2, c3;
        cin >> l1 >> c1 >> l2 >> c2 >> l3 >> c3;
        bool r1 = c1 == 'R';
        bool r2 = c2 == 'R';
        bool r3 = c3 == 'R';
        adj[l1*2-!r1].push_back(l2*2-r2);
        adj[l1*2-!r1].push_back(l3*2-r3);
        adj[l2*2-!r2].push_back(l1*2-r1);
        adj[l2*2-!r2].push_back(l3*2-r3);
        adj[l3*2-!r3].push_back(l1*2-r1);
        adj[l3*2-!r3].push_back(l2*2-r2);
    }

	for(int i=1; i<=2*k; i++) {
		if(!closed[i]) tarjanSCC(i);
	}

    vector<int> compo_num(2*k+1);
    for(int i=0; i<scc.size(); i++) {
        for(int v : scc[i]) {
            compo_num[v] = i;
        }
    }

    vector<vector<int>> compo_adj(scc.size());
    vector<int> in(scc.size(), 0);
    for(int i=1; i<=2*k; i++) {
        for(int to : adj[i]) {
            compo_adj[compo_num[i]].push_back(compo_num[to]);
            in[compo_num[to]]++;
        }
    }

    queue<int> starts;
    for(int i=0; i<scc.size(); i++) {
        if(in[i] == 0) starts.push(i);
    }

    bool fail = false;
    for(int i=0; i<scc.size(); i++) {
        // check if other colors are in the component
        sort(scc[i].begin(), scc[i].end());
        bool other = false;
        for(int j=1; j<scc[i].size(); j++) {
            if(scc[i][j-1] % 2 == 1 && scc[i][j-1] + 1 == scc[i][j]) {
                other = true;
                break;
            }
        }

        if(other) {
            fail = true;
            break;
        }
    }

	if(fail) cout << -1;
    else {
        string answer;
        answer.resize(k);

        vector<bool> b(2*k+1, false);

        for(int i=(int)scc.size() - 1; i>=0; i--) {
            for(int u : scc[i]) {
                int v;
                if(u % 2 == 0) v = u - 1;
                else v = u + 1;
                b[v] = !b[u];
            }
        }

        for(int i=2; i<=2*k; i+=2) {
            if(b[i])
                answer[i/2-1] = 'B';
            else
                answer[i/2-1] = 'R';
        }

        cout << answer;
    }

	return 0;
}