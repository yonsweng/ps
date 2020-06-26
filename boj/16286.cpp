#include <iostream>
#include <algorithm>

#define MAXN 500001

using namespace std;

int a[MAXN], s[MAXN];
bool d[MAXN];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int w, n;
	cin >> w >> n;

	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		s[i] = s[i - 1] + a[i];
	}

	int fair = 0;
	int min_x = 0, max_x = w;  // Search [0, w].
	while (min_x <= max_x) {
		int x = (min_x + max_x) / 2;  // [x, w]
		int l = 0, r = 0, t = -1;

		d[0] = true;
		for (int i = 1; i <= n; i++) {
			while (s[i] - s[l] > w) l++;
			while (s[i] - s[r] >= x) {
				if (d[r]) t = r;
				r++;
			}
			d[i] = (l <= t) ? true : false;
		}

		if (d[n]) {  // increase x
			fair = max(fair, x);
			min_x = x + 1;
		}
		else {  // decrease x
			max_x = x - 1;
		}
	}

	long long answer = (long long)(w - fair) * (long long)(w - fair);
	cout << answer;

	return 0;
}