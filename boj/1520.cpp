/*
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
*/

#include <iostream>
#include <algorithm>

using namespace std;

const int di[] = {0, 0, 1, -1}, dj[] = {1, -1, 0, 0};
int m, n;
int d[502][502], memo[502][502];

int num_cases(int i, int j)
{
	if(memo[i][j] >= 0) return memo[i][j];

	int sum = 0;
	for(int k=0; k<4; k++) {
		if(d[i+di[k]][j+dj[k]] > d[i][j]) {
			sum += num_cases(i+di[k], j+dj[k]);
		}
	}

	return memo[i][j] = sum;
}

int main()
{
	// freopen("1.in", "r", stdin);
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> m >> n;
	for(int i=1; i<=m; i++) {
		for(int j=1; j<=n; j++) {
			cin >> d[i][j];
		}
	}

	fill_n(memo[0], 502*502, -1);
	memo[1][1] = 1;

	cout << num_cases(m, n);

	return 0;
}