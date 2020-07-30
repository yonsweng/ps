#include <iostream>

using namespace std;

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int q;
	cin >> q;

	while(q--) {
		int n;
		cin >> n;

		int answer;
		if(n == 2) answer = 2;
		else if(n % 2 == 1) answer = 1;
		else answer = 0;

		cout << answer << '\n';
	}

	return 0;
}