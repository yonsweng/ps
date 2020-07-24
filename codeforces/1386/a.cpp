#include <bits/stdc++.h>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    while(T--) {
        int n, m;
        cin >> n >> m;
        int a[1000], b[1000];
        for(int i=0; i<n; i++) {
            cin >> a[i];
        }
        for(int i=0; i<m; i++) {
            cin >> b[i];
        }
        bool stop = false;
        int answer;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(a[i] == b[j]) {
                    stop = true;
                    answer = a[i];
                    break;
                }
            }
            if(stop) break;
        }
        if(stop) {
            cout << "YES\n";
            cout << "1 " << answer << '\n';
        } else {
            cout << "NO\n";
        }
    }
}