#include <iostream>

using namespace std;

int price[100001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, w;
	cin >> n >> w;

	for(int i=1; i<=n; i++) {
		cin >> price[i];
	}

	long long coin = 0, cash = w;

	for(int i=1; i<=n-1; i++) {
		if(price[i+1] > price[i]) {
			coin += cash / price[i];
			cash -= (cash / price[i]) * price[i];
		}
		else if(price[i+1] < price[i]) {
			cash += coin * price[i];
			coin = 0;
		}
	}
	cash += coin * price[n];

	cout << cash;

	return 0;
}