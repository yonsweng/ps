#include <iostream>
#include <vector>
 
using namespace std;
 
int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);
 
    int t;
    cin >> t;
    while(t-- > 0) {
        int n;
        cin >> n;
        vector<int> a(n);
        for(int i=0; i<n; i++) cin >> a[i];
 
        if(a[0] < a[n-1]) cout << "YES\n";
        else cout << "NO\n";
    }
 
    return 0;
}