#include <iostream>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    int t;
    cin >> t;
    while(t--) {
        int a[100000], n;
        cin >> n;
        for(int i=0; i<n; i++) {
            cin >> a[i];
        }

        int i = 0, j = 1;
        while(j < n) {
            for( ; i < n-1 && a[i] <= 0; i++);
            if(i == n-1) break;

            for(j = max(j, i+1); j < n; j++) {
                if(a[j] >= 0) continue;
                int d = min(a[i], -a[j]);
                a[i] -= d;
                a[j] += d;
                if(a[i] == 0) break;
            }
        }

        long long sum = 0;
        for(int i=0; i<n; i++) {
            if(a[i] > 0) {
                sum += a[i];
            }
        }
        cout << sum << '\n';
    }
}