#include <cstdio>
#include <algorithm>

int main()
{
    // freopen("1.in", "r", stdin);
	int t;
    scanf("%d", &t);
    while(t--) {
        int n, p, k, i, a[200001], d[200001] = {};
        scanf("%d %d %d", &n, &p, &k);
        for(i=1; i<=n; i++)
            scanf("%d", &a[i]);

        std::sort(a+1, a+1+n);

        // d[i]: i개의 goods를 사기 위한 최소 coin 수
        i = 1;
        d[i] = a[i];
        if(d[i] <= p)
            for(i=2; i<=n; i++) {
                d[i] = d[i-2] + a[i];
                if(d[i] > p) break;
            }
        
        printf("%d\n", i-1);
    }
	return 0;
}