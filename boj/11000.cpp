#include <iostream>
#include <algorithm>

using namespace std;

pair<int, int> t[400000];

int main()
{
	//freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	for(int i=0; i<N; i++) {
		int S, T;
		cin >> S >> T;

		t[i*2] = make_pair(S, 1);
		t[i*2+1] = make_pair(T, -1);
	}

	sort(t, t+2*N);

	int num = 0, cnt = 0;
	for(int i=0; i<2*N; i++) {
		cnt += t[i].second;
		num = max(num, cnt);
	}

	cout << num;

	return 0;
}