#include <bits/stdc++.h>

using namespace std;

int st[262143][26];

void construct_st(string &s, int l, int r, int i) {
    if(l + 1 == r) {
        st[i][s[l]-'a'] = 1;
        for(int j=0; j<26; j++) {
            if(s[l]-'a' != j) {
                st[i][j] = 0;
            }
        }
    } else {
        int m = (l + r) / 2;
        construct_st(s, l, m, i*2+1);
        construct_st(s, m, r, i*2+2);
        for(int j=0; j<26; j++) {
            st[i][j] = st[i*2+1][j] + st[i*2+2][j];
        }
    }
}

// count c in [l, r)
int get_count(int ql, int qr, int c, int l, int r, int i) {
    if(qr <= l || r <= ql) {
        return 0;
    }
    if(ql == l && qr == r) {
        return st[i][c];
    }
    int m = (l + r) / 2;
    return get_count(ql, qr, c, l, m, i*2+1) + get_count(ql, qr, c, m, r, i*2+2);
}

int f(int l, int r, int c, int n) {
    if(l + 1 == r) {
        return 1 - get_count(l, r, c, 0, n, 0);
    }
    int m = (l + r) / 2;
    int left_changes = (r - l) / 2 - get_count(l, m, c, 0, n, 0);
    int right_changes = (r - l) / 2 - get_count(m, r, c, 0, n, 0);
    return min(left_changes + f(m, r, c+1, n), right_changes + f(l, m, c+1, n));
}

int main() {
    int t;

    ios::sync_with_stdio(false), cin.tie(NULL);

    cin >> t;

    while(t--) {
        int n;
        string s;

        cin >> n >> s;

        construct_st(s, 0, n, 0);

        cout << f(0, n, 0, n) << '\n';
    }
}