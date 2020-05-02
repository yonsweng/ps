#include <iostream>

using namespace std;

int d[100][100];

int main()
{
	int t;
	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		int m, n;
		cin >> m >> n;

		for(int y=0; y<m; y++) {
			for(int x=0; x<n; x++) {
				cin >> d[y][x];
			}
		}

		int sum = 0;

		for(int x=0; x<n; x++) {
			int cnt = 0;
			for(int y=m-1; y>=0; y--) {
				if(d[y][x] == 1) {
					sum += (m - 1 - cnt++) - y;
				}
			}
		}

		cout << sum << endl;
	}
	return 0;
}