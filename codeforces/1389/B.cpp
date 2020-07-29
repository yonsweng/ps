#include <iostream>
#include <string>

using namespace std;

int d[6][100001] = {};

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, k, z;
        cin >> n >> k >> z;

        int a[100001] = {};
        for(int i=1; i<=n; i++) {
            cin >> a[i];
        }

        d[0][1] = a[1];
        for(int j=2; j<=k+1; j++) {
            d[0][j] = d[0][j-1] + a[j];
        }
        for(int i=1; i<=z; i++) {
            for(int j=1; j<=k+1-i*2; j++) {
                d[i][j] = max(d[i][j-1]+a[j], d[i-1][j+1]+a[j]);
            }
        }

        int answer = 0;
        for(int i=0; i<=z; i++) {
            for(int j=1; j<=k+1-i*2; j++) {
                answer = max(answer, d[i][j]);
            }
        }
        cout << answer << '\n';
    }
}