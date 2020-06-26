#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	//freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, L;
	cin >> N >> L;

	int x[1000];
	for(int i=0; i<N; i++)
		cin >> x[i];

	sort(x, x+N);

	int end = 1, cnt = 0;
	for(int i=0; i<N; i++) {
		if(x[i] >= end) {
			end = x[i] + L;
			cnt++;
		}
	}

	cout << cnt;

	return 0;
}