#include <bits/stdc++.h>

using namespace std;

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int q;
	cin >> q;

	while(q--) {
		int n, color[30], even = 0, odd = 0;

		cin >> n;
		for(int i=0; i<n; i++) {
			cin >> color[i];
			if(i % 2 == 0)
				even += color[i];
			else
				odd += color[i];
		}

		if(n % 2 == 1)
			cout << "YES\n";
		else
			if(abs(even - odd) <= 1)
				cout << "YES\n";
			else
				cout << "NO\n";
	}

	return 0;
}