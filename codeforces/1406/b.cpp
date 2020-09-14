#include <bits/stdc++.h>

using namespace std;

bool comp(int a, int b) {
    return abs(a) > abs(b);
}

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        int a[200001];
        for(int i=1; i<=n; i++) {
            cin >> a[i];
        }

        // -9 -7 -5 -3 -2 1
        sort(a + 1, a + 1 + n, comp);
        // for(int i=1; i<=n; i++) {
        //     cout << a[i] << ' ';
        // }
        // cout << '\n';

        // m: # of negative numbers
        long long best = -243000000000000000LL;
        for(int m=0; m<=5; m++) {
            long long p1 = 1, p2 = 1;
            int cnt1 = 0, cnt2 = 0;

            for(int i=1; i<=n; i++) {
                if(cnt1 < m && a[i] < 0) {
                    cnt1++;
                    p1 *= a[i];
                }
            }

            for(int i=n; i>=1; i--) {
                if(cnt2 < m && a[i] < 0) {
                    cnt2++;
                    p2 *= a[i];
                }
            }

            for(int i=1; i<=n; i++) {
                if(cnt1 < 5 && a[i] >= 0) {
                    cnt1++;
                    p1 *= a[i];
                }
            }

            for(int i=n; i>=1; i--) {
                if(cnt2 < 5 && a[i] >= 0) {
                    cnt2++;
                    p2 *= a[i];
                }
            }
            
            if(cnt1 != 5)
                p1 = -243000000000000000LL;
            
            if(cnt2 != 5)
                p2 = -243000000000000000LL;

            best = max(best, p1);
            best = max(best, p2);
        }

        cout << best << '\n';
    }
}