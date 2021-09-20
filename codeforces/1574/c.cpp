#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int n;
    cin >> n;
    vector<ll> a(n);
    for(int i=0; i<n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    ll s = std::accumulate(a.begin(), a.end(), decltype(a)::value_type(0));
    int m;
    cin >> m;
    for(int i=0; i<m; i++) {
        ll x, y;
        cin >> x >> y;
        int j = lower_bound(a.begin(), a.end(), x) - a.begin();
        if(j == n) j = n - 1;
        if(j == 0) j = 1;
        ll answer1 = max(x - a[j-1], 0LL) + max(y - (s - a[j-1]), 0LL);
        ll answer2 = max(x - a[j], 0LL) + max(y - (s - a[j]), 0LL);
        ll answer = min(answer1, answer2);
        cout << answer << '\n';
    }
}