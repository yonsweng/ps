#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

#define INF 999999999

using namespace std;

int d[20001];
vector<vector<pair<int, int> > > vt;

int main()
{
	//freopen("input.txt", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m;
	cin >> n >> m;

	vt.resize(n+1);

	while(m--) {
		int a, b, t;
		cin >> a >> b >> t;

		vt[a].push_back({b, t});
		vt[b].push_back({a, t});
	}

	int robot[3];
	cin >> robot[0] >> robot[1] >> robot[2];

	int max_time[20001] = {};

	for(int r=0; r<3; r++) {
		int start = robot[r];
		fill_n(d, n+1, -1);

		priority_queue<pair<int, int> > pq;
		pq.push({0, start});

		while(pq.size()) {
			int here = pq.top().second;
			int cost = -pq.top().first;
			pq.pop();

			if(d[here] != -1)
				continue;

			d[here] = cost;
			for(auto it : vt[here]) {
				int next = it.first;
				int acost = -it.second - cost;
				if(d[next] != -1)
					continue;
				pq.push({acost, next});
			}
		}

		// for(int i=1; i<=n; i++) {
		// 	cout << d[i] << ' ';
		// }
		// cout << endl;

		for(int i=1; i<=n; i++) {
			max_time[i] = max(max_time[i], d[i]);
		}
	}

	int minimum = INF;
	for(int i=1; i<=n; i++) {
		minimum = min(minimum, max_time[i]);
	}

	cout << minimum;

	return 0;
}