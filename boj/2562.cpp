#include <iostream>
#include <vector>

using namespace std;

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n = 9;
    vector<int> a(n);
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }
    int max_val = 0, mi = 0;
    for(int i=0; i<n; i++) {
        if(a[i] > max_val) {
            max_val = a[i];
            mi = i;
        }
    }

    cout << max_val << '\n' << mi + 1;
}