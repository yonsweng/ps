#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int d[50001];

int main()
{
	freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	fill_n(d, n+1, 9);
	d[0] = 0;

	for(int i=1; i<=(int)sqrt(n) + 1; i++) {
		int isq = i * i;
		for(int j=isq; j<=n; j++) {
			d[j] = min(d[j], d[j-isq] + 1);
		}
	}

	// for(int i=1; i<=n; i++) {
	// 	cout << d[i] << ' ';
	// }
	cout << d[n];

	return 0;
}