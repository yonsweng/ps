#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);
    
    int n;
    cin >> n;

    vector<int> a(n);
    for(int i=0; i<n; i++)
        cin >> a[i];

    int max_val = 0, min_val = 987654321;
    for(int i=0; i<n; i++) {
        max_val = max(max_val, a[i]);
        min_val = min(min_val, a[i]);
    }

    cout << min_val << ' ' << max_val;
}