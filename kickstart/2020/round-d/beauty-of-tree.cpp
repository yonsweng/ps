#include <cstdio>

int main() {
    // freopen("1.in", "r", stdin);
    int t;
    scanf("%d", &t);
    for(int case_num=1; case_num<=t; case_num++) {
        int n, a, b;
        scanf("%d %d %d", &n, &a, &b);
        int p[101] = {};
        for(int i=2; i<=n; i++) {
            scanf("%d", &p[i]);
        }
        long long tot_pnt = 0;
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                bool c[101] = {};
                int cnt = a;
                for(int k=i; k!=0; k=p[k]) {
                    if(cnt == a) {
                        c[k] = true;
                        cnt = 0;
                    }
                    cnt++;
                }
                cnt = b;
                for(int k=j; k!=0; k=p[k]) {
                    if(cnt == b) {
                        c[k] = true;
                        cnt = 0;
                    }
                    cnt++;
                }
                int pnt = 0;
                for(int k=1; k<=n; k++) {
                    if(c[k]) {
                        pnt++;
                    }
                }
                tot_pnt += pnt;
            }
        }
        double ans = (double)tot_pnt / (n * n);
        printf("Case #%d: %.7f\n", case_num, ans);
    }
    return 0;
}