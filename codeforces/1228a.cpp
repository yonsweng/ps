#include <iostream>

using namespace std;

int main()
{
	//freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int l, r;
	cin >> l >> r;

	for(int x=l; x<=r; x++) {
		bool check[10] = {}, ok = true;
		int n = x;
		while(n) {
			if(!check[n % 10]) {
				check[n%10] = true;
			}
			else {
				ok = false;
				break;
			}
			n /= 10;
		}

		if(ok) {
			cout << x;
			exit(0);
		}
	}

	cout << -1;

	return 0;
}