#include <bits/stdc++.h>

using namespace std;

int n;
int a[100000];

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    while(T--) {
        cin >> n;
        for(int i=0; i<n; i++) {
            cin >> a[i];
        }
        int cnt = 0;
        for(int i=0; i<n-1; i++) {
            if(a[i] != 1) {
                break;
            } else {
                cnt++;
            }
        }
        if(cnt % 2 == 0) cout << "First\n";
        else cout << "Second\n";
    }
}