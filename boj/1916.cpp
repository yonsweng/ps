#include <cstdio>

int d[1001][1001];
int p[1001];  // Minimum price
bool c[1001];  // Closed set

int main()
{
	freopen("input.txt", "r", stdin);
	int n, m;
	scanf("%d%d", &n, &m);
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=n; j++) {
			d[i][j] = 999999999;
		}
		d[i][i] = 0;
	}
	for(int i=0; i<m; i++) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		d[a][b] = (c < d[a][b]) ? c : d[a][b];
	}
	int a, b;
	scanf("%d %d", &a, &b);

	for(int i=1; i<=n; i++) {
		p[i] = d[a][i];
	}
	c[a] = true;

	// Djikstra algorithm
	for(int i=1; i<=n; i++) {
		int min = 999999999, mi = 0;
		for(int j=1; j<=n; j++) {
			if(!c[j] && p[j] < min) {
				min = p[j];
				mi = j;
			}
		}
		if(mi == 0 || mi == b) break;

		c[mi] = true;

		for(int j=1; j<=n; j++) {
			if(!c[j] && p[mi] + d[mi][j] < p[j]) {
				p[j] = p[mi] + d[mi][j];
			}
		}
	}

	printf("%d", p[b]);
	return 0;
}