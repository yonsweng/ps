#include <bits/stdc++.h>

#define MAXN 300

using namespace std;

int gcd(int n1, int n2) {
    while (n1 != n2) {
        if (n1 > n2)
            n1 -= n2;
        else
            n2 -= n1;
    }
    return n1;
}

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; case_num++) {
        int N;
        pair<int, int> cj[MAXN];

        cin >> N;
        for (int i = 0; i < N; i++) cin >> cj[i].first >> cj[i].second;

        set<pair<int, int>> s;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i == j) continue;
                int a = cj[j].second - cj[i].second;
                int b = cj[i].first - cj[j].first;
                if ((long long) a * b > 0) {
                    int g = gcd(a, b);
                    a /= g;
                    b /= g;
                    s.emplace(a, b);
                }
            }
        }

        cout << "Case #" << case_num << ": " << s.size() + 1 << '\n';
    }

    return 0;
}