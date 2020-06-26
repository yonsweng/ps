#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

vector<int> work[1001];

int main()
{
	//freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	for(int i=0; i<n; i++) {
		int d, w;
		cin >> d >> w;

		work[d].push_back(w);
	}

	priority_queue<int> pq;
	int point = 0;

	for(int day=1000; day>=1; day--) {
		for(int w : work[day]) {
			pq.push(w);
		}

		if(!pq.empty()) {
			point += pq.top();
			pq.pop();
		}
	}

	cout << point;

	return 0;
}