#include <iostream>
#include <cstring>

using namespace std;

long long d[21][21][21];

long long dynamic(int n, int l, int r)
{
	if(d[n][l][r]) return d[n][l][r];
	if(l <= 0 || r <= 0 || n == 0 || l + r > n + 1) return 0;

	d[n][l][r] = dynamic(n-1, l-1, r) + dynamic(n-1, l, r-1) + (n-2) * dynamic(n-1, l, r);
	return d[n][l][r];
}

int main()
{
	//freopen("input.txt", "r", stdin);

	int t;
	cin >> t;

	for(int test_case=1; test_case<=t; test_case++) {
		int n, l, r;
		cin >> n >> l >> r;

		memset(d, 0, sizeof(d));
		d[1][1][1] = 1;

		cout << dynamic(n, l, r) << endl;
	}

	return 0;
}