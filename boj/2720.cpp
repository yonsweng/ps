#include <iostream>

using namespace std;

int main()
{
	//freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	while(N--) {
		int C;
		cin >> C;

		int q, d, n, p;

		q = C / 25;
		C = C % 25;

		d = C / 10;
		C = C % 10;

		n = C / 5;
		C = C % 5;

		p = C;

		cout << q << ' ' << d << ' ' << n << ' ' << p << '\n';
	}

	return 0;
}