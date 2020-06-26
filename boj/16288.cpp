#include <iostream>
#include <queue>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, k;
	cin >> n >> k;

	int order[101];
	for (int i = 1; i <= n; i++) {
		cin >> order[i];
	}

	queue<int> q[101];  // k queues.
	bool answer = true;

	for (int now = 1, i = 1; now <= n; now++) {
		// must pull out now.
		while (i <= n) {
			bool pulled = false;
			for (int j = 1; j <= k; j++) {
				if (!q[j].empty() && q[j].front() == now) {
					q[j].pop();
					pulled = true;
					break;
				}
			}
			if (pulled) continue;

			// back이 가장 큰 queue에 넣어야?
			int mj = 0, max_back = -1;
			for (int j = 1; j <= k; j++) {
				if (!q[j].empty() && max_back < q[j].back() && q[j].back() < order[i]) {
					mj = j;
					max_back = q[j].back();
				}
				else if (max_back == -1 && q[j].empty()) {
					mj = j;
					max_back = 0;
				}
			}

			if (mj > 0) {
				q[mj].push(order[i]);
			}
			else {
				answer = false;
				break;
			}

			i++;
		}
		
		if (answer == false) break;
	}

	if (answer) cout << "YES";
	else cout << "NO";

	return 0;
}