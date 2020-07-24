#include <iostream>
#include <vector>
using namespace std;
int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;

        vector<int> a(n+1);
        for(int i=1; i<=n; i++) {
            cin >> a[i];
        }

        int answer = 0;
        bool found_increase = false;
        for(int i=n-1; i>=1; i--) {
            if(a[i] < a[i+1]) {
                found_increase = true;
            } else if(found_increase && a[i] > a[i+1]) {
                answer = i;
                break;
            }
        }

        cout << answer << '\n';
    }
}