#include <bits/stdc++.h>

using namespace std;

char a[100][10001];

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int T;
    cin >> T;
    for(int x=1; x<=T; x++) {
        double P;
        cin >> P;
        for(int i=0; i<100; i++)
            cin >> a[i];

        pair<int, int> s[10000] = {};
        for(int j=0; j<10000; j++) {
            for(int i=0; i<100; i++)
                s[j].first += int(a[i][j] - '0');
            s[j].second = j;
        }

        sort(s, s + 10000);

        int cnt[100] = {};
        for(int i=0; i<100; i++) {
            for(int j=0; j<100; j++) {
                cnt[i] += int(a[i][s[j].second] - '0');
            }
        }

        int max_val = cnt[0], max_idx = 0;
        for(int i=1; i<100; i++) {
            if(cnt[i] > max_val) {
                max_val = cnt[i];
                max_idx = i;
            }
        }

        cout << "Case #" << x << ": " << max_idx + 1 << '\n';
    }
}