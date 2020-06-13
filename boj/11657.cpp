#include <iostream>
#include <vector>

#define INF 99999999

using namespace std;

vector<pair<int, int> > adj[501];

int main()
{
	// freopen("1.in", "r", stdin);

	int n, m;
	cin >> n >> m;
	for(int i=0; i<m; i++) {
		int from, to, time;
		cin >> from >> to >> time;
        adj[from].emplace_back(to, time);
	}

	long long t[501];  // t[v] : minimum time 1 -> v
	fill_n(t, n+1, INF);
	t[1] = 0;

    bool cycle = false;

	for(int i=0; i<n; i++) {
        for(int j=1; j<=n; j++) {
            for(pair<int, int> to_time : adj[j]) {
                int to = to_time.first, time = to_time.second;
                if(t[j] != INF && t[to] > t[j] + time) {
                    t[to] = t[j] + time;
                    if(i == n-1) cycle = true;
                }
            }
        }
    }

    if(t[1] < 0 || cycle) cout << -1;
    else for(int i=2; i<=n; i++)
        cout << (t[i] == INF ? -1 : t[i]) << '\n';

	return 0;
}