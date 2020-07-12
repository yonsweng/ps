#include <cstdio>
#include <cmath>

int main() {
    int t;
    scanf("%d", &t);
    while(t--) {
        int n;
        scanf("%d", &n);
        bool done = false;
        for(int d=2; d<=sqrt(n); d++) {
            if(n % d == 0) {
                printf("%d %d\n", n/d, n-n/d);
                done = true;
                break;
            }
        }
        if(!done) {
            printf("%d %d\n", 1, n-1);
        }
    }
    return 0;
}