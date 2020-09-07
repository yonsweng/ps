#include <iostream>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    int t;
    cin >> t;
    while(t--) {
        int a[100], n;
        cin >> n;
        for(int i=0; i<n; i++) {
            cin >> a[i];
        }

        for(int i=n-1; i>=0; i--) {
            cout << a[i] << ' ';
        }
        cout << '\n';
    }
}