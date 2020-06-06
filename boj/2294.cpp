#include <cstdio>
#include <algorithm>
#include <ctime>

#define INF 999999

int n, v[100], d[100001];

int dp(int k) {
    if(k < 0) return INF;
    if(k == 0) return 0;
    if(d[k]) return d[k];

    int m = INF;
    for(int i=0; i<n; i++) {
        int coins = dp(k-v[i]) + 1;
        m = std::min(m, coins);
    }
    return d[k] = m;
}

int main()
{
    clock_t start = clock();

    freopen("1.in", "r", stdin);
    int k;
    scanf("%d %d", &n, &k);
    for(int i=0; i<n; i++)
        scanf("%d", &v[i]);

    int ans = dp(k);
    if(ans == INF) printf("-1");
    else printf("%d", ans);

    clock_t end = clock();
    printf("\n%f", (end-start)/CLOCKS_PER_SEC);

	return 0;
}