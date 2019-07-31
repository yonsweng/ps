#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		int n;
		cin >> n;

		int p[1001];
		for(int i=1; i<=n; i++) {
			cin >> p[i];
		}

		int g[1001] = {0, }, cnt = 0;
		for(int i=1; i<=n; i++) {
			if(g[i] != 0) continue;

			cnt++;

			int j = i;
			while(g[j] == 0) {
				g[j] = cnt;
				j = p[j];
			}
		}

		cout << cnt << endl;
	}

	return 0;
}