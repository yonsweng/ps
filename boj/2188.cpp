#include <iostream>

#define MAXN 201
#define MAXM 201

using namespace std;

// i번째 소가 매칭될 수 있으면 1, 없으면 0.
bool match(bool g[][MAXM], int cih[], bool visited[], int n, int m, int i)
{
	if (!visited[i]) {
		visited[i] = true;

		for (int j = 1; j <= m; j++) {
			if (g[i][j]) {
				if (cih[j] == 0 || match(g, cih, visited, n, m, cih[j])) {
					cih[j] = i;
					return true;
				}
			}
		}
	}

	return false;
}

int main()
{
	bool g[MAXN][MAXM] = { {false,} , };  // g[i][j] : i번째 소가 j번째 축사를 선호한다면 true.
	int cih[MAXM] = { 0, };  // cih[j] : j번째 축사에 있는 소의 번호.
	int n, m;  // n:소의 마릿수, m:축사의 개수
	cin >> n >> m;
	
	for (int i = 1; i <= n; i++) {
		int si;
		cin >> si;
		for (int j = 1; j <= si; j++) {
			int house;
			cin >> house;
			g[i][house] = true;  // i번째 소가 house번째 축사를 선호한다.
		}
	}

	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		bool visited[MAXN] = { 0, };
		if (match(g, cih, visited, n, m, i)) {
			cnt++;
		}
	}

	cout << cnt;

	return 0;
}