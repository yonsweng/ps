#include <cstdio>
#include <algorithm>

int d[2][100001];

int main()
{
    // freopen("1.in", "r", stdin);
    int n, k, w[100], v[100];
    scanf("%d %d", &n, &k);
    for(int i=0; i<n; i++)
        scanf("%d %d", &w[i], &v[i]);

    for(int i=0; i<n; i++) {
        for(int j=0; j<w[i]; j++)
            d[i%2][j] = d[(i+1)%2][j];
        for(int j=w[i]; j<=k; j++)
            d[i%2][j] = std::max(d[(i+1)%2][j], d[(i+1)%2][j-w[i]] + v[i]);
    }

    printf("%d", d[(n-1)%2][k]);
	return 0;
}