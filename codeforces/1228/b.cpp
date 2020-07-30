#include <iostream>

using namespace std;

int d[1000][1000];

int main()
{
	freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int h, w;
	cin >> h >> w;

	for(int i=0; i<h; i++) {
		int n;
		cin >> n;

		for(int j=0; j<n; j++) {
			if(d[i][j] == 2) {
				cout << 0;
				exit(0);
			}
			d[i][j] = 1;
		}

		if(n < w) {
			if(d[i][n] == 1) {
				cout << 0;
				exit(0);
			}
			d[i][n] = 2;
		}
	}

	for(int j=0; j<w; j++) {
		int n;
		cin >> n;

		for(int i=0; i<n; i++) {
			if(d[i][j] == 2) {
				cout << 0;
				exit(0);
			}
			d[i][j] = 1;
		}

		if(n < h) {
			if(d[n][j] == 1) {
				cout << 0;
				exit(0);
			}
			d[n][j] = 2;
		}
	}

	int cnt = 0;
	for(int i=0; i<h; i++) {
		for(int j=0; j<w; j++) {
			if(d[i][j] == 0) {
				cnt++;
			}
		}
	}

	int product = 1;
	for(int i=0; i<cnt; i++) {
		product = (product * 2) % 1000000007;
	}

	cout << product;

	return 0;
}