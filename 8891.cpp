#include <iostream>

using namespace std;

pair<int, int> d[10000];

int main()
{
	//freopen("input.txt", "r", stdin);

	int x = 1, y = 1, initial_y = 1;
	for(int n=1; n<10000; n++) {
		d[n] = make_pair(x, y);

		if(y == 1) {
			x = 1;
			y = ++initial_y;
		}
		else {
			x++;
			y--;
		}
	}

	int t;
	cin >> t;

	for(int test_case=1; test_case<=t; test_case++) {
		int a, b;
		cin >> a >> b;

		pair<int, int> sum = make_pair(d[a].first+d[b].first, d[a].second+d[b].second);

		int k = sum.first + sum.second - 1;
		int answer = k * (k - 1) / 2 + sum.first;

		cout << answer << endl;
	}

	return 0;
}