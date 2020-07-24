#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);
    int t;
    cin >> t;
    while(t--) {
        int n, a[101];
        cin >> n;
        for(int i=1; i<=2*n; i++) {
            cin >> a[i];
        }
        bool check[51] = {};
        for(int i=1; i<=2*n; i++) {
            if(!check[a[i]]) {
                check[a[i]] = true;
                cout << a[i] << ' ';
            }
        }
        cout << '\n';
    }
}