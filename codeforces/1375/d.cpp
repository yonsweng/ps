#include <iostream>
#include <vector>

using namespace std;

int find_mex(vector<int> &a, int n) {
    vector<bool> check(n+1, false);
    for(int ai : a) {
        check[ai] = true;
    }
    for(int i=0; i<=n; i++) {
        if(!check[i]) return i;
    }
    return n;
}

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

        vector<int> ans;

        while(true) {
            int mex = find_mex(a, n);
            bool increasing = true;
            for(int i=0; i<n-1; i++) {
                if(a[i] > a[i+1]) {
                    if(mex >= a[i]) {
                        a[i+1] = mex;
                        ans.push_back(i+1);
                    } else {
                        a[i] = mex;
                        ans.push_back(i);
                    }
                    increasing=false;
                }
            }
            if(increasing) break;
        }

        cout << ans.size() << '\n';
        for(int a : ans) {
            cout << a + 1 << ' ';
        }
        cout << '\n';
    }

    return 0;
}