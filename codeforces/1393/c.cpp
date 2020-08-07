#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--) {
        int n;
        cin >> n;
        int a[100001], c[100001] = {};
        for(int i=1; i<=n; i++) {
            cin >> a[i];
            c[a[i]]++;
        }
        int m = 0;
        for(int i=1; i<=n; i++) {
            if(c[i] > m) {
                m = c[i];
            }
        }

        int mcnt = 0, cnt = 0;
        for(int i=1; i<=n; i++) {
            if(c[i] == m) {
                mcnt++;
            }
        }

        cout << (n - mcnt * m) / (m - 1) + (mcnt - 1) << '\n';
    }
}