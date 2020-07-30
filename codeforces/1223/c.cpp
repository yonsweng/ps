#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define INF 999999999

using namespace std;

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int q;
	cin >> q;
	while(q--) {
		int n, p[200000], x, a, y, b;
		long long k;

		cin >> n;
		for(int i=0; i<n; i++)
			cin >> p[i];
		cin >> x >> a;
		cin >> y >> b;
		cin >> k;

		vector<int> order, ratio;
		for(int i=1; i<=n; i++)
			if(i % a == 0 && i % b == 0) {
				order.push_back(i);
				ratio.push_back(x+y);
			}
			else if(i % a == 0) {
				order.push_back(i);
				ratio.push_back(x);
			}
			else if(i % b == 0) {
				order.push_back(i);
				ratio.push_back(y);
			}
		int m = order.size();

		sort(p, p+n, greater<int>());

		int lower = 0, upper = m - 1, answer = INF;
		while(lower <= upper)
		{
			int mid = (lower + upper) / 2;

			vector<int> tmp_ratio;
			tmp_ratio.assign(ratio.begin(), ratio.begin() + mid + 1);
			sort(tmp_ratio.begin(), tmp_ratio.end(), greater<int>());

			long long contrib = 0;
			for(int i=0; i<=mid; i++)
				contrib += p[i] / 100 * tmp_ratio[i];

			if(contrib >= k) {
				answer = min(answer, order[mid]);
				upper = mid - 1;
			}
			else
				lower = mid + 1;
		}

		if(answer == INF) answer = -1;
		cout << answer << '\n';
	}

	return 0;
}