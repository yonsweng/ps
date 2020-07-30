#include <cstdio>
#include <cmath>

int main() {
    int t;
    scanf("%d", &t);
    while(t--) {
        int n;
        scanf("%d", &n);
        int a[200001];
        for(int i=1; i<=n; i++) {
            scanf("%d", &a[i]);
        }
        // all are inplace
        bool inplace = true;
        for(int i=1; i<=n; i++) {
            if(a[i] != i) {
                inplace = false;
                break;
            }
        }
        if(inplace) {
            printf("0\n");
            continue;
        }
        // no is inplace
        inplace = false;
        for(int i=1; i<=n; i++) {
            if(a[i] == i) {
                inplace = true;
                break;
            }
        }
        if(!inplace) {
            printf("1\n");
            continue;
        }
        // two end is inplace
        if(a[1] == 1 && a[n] == n) {
            inplace = false;
            // some is inplace -> 3
            // no one is inplace -> 2
            for(int i=2; i<=n-1; i++) {
                if(a[i] == i) {
                    inplace = true;
                    break;
                }
            }
            if(inplace)
                printf("3\n");
            else
                printf("2\n");
            continue;
        }
        // else
        printf("2\n");
    }
    return 0;
}