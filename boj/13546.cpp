#include <iostream>

using namespace std;

int query(int l, int r) {

}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int n, k, m, l, r, a[100001];

    for(int i=1; i<=n; i++)
        cin >> a[i];

    cin >> m;
    for(int i=1; i<=m; i++) {
        cin >> l >> r;
        cout << query(l, r) << '\n';
    }

    return 0;
}