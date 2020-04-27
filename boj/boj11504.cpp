#include <iostream>

using namespace std;

int main()
{
	//freopen("input.txt", "r", stdin);

	int t;
	cin >> t;

	for(int test_case=0; test_case<t; test_case++) {
		int n, m, a[9], b[9], x = 0, y = 0;
		cin >> n >> m;
		int p = 1;
		for(int i=0; i<m-1; i++) {
			p *= 10;
		}
		int pp = p;
		for(int i=0; i<m; i++) {
			cin >> a[i];
			x += a[i] * p;
			p = p / 10;
		}
		p = pp;
		for(int i=0; i<m; i++) {
			cin >> b[i];
			y += b[i] * p;
			p = p / 10;
		}

		int c[100];
		for(int i=0; i<n; i++) {
			cin >> c[i];
		}

		int cnt = 0;

		for(int i=0; i<n; i++) {
			int z = 0;
			p = pp;
			for(int j=i; j<i+m; j++) {
				z += c[j%n] * p;
				p = p / 10;
			}
			if(x <= z && z <= y) {
				cnt++;
			}
		}

		cout << cnt << endl;
	}
	return 0;
}