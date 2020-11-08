#include <bits/stdc++.h>

using namespace std;
using pi = pair<int, int>;
const int SIZE = 200000;
int N, start_end[SIZE];

int main() {
    cin >> N;
    vector<pi> v(2 * N);
    for (int i = 0; i < N; i++) {
        cin >> v[i * 2].first;
        v[i * 2].second = 1;
        cin >> v[i * 2 + 1].first;
        v[i * 2 + 1].second = -v[i * 2].first;
    }
    sort(v.begin(), v.end());
    fill(start_end, start_end + SIZE, 1e9);

    int count1 = 0, count2 = 0, ans1 = 0, ans2 = 0;
    for (auto p : v) {
        int t, i;
        t = p.first; i = p.second;
        if (i < 0) { // end
            count2--;
            ans1 = max(ans1, count1 - start_end[-i]);
        } else { // start
            start_end[t] = min(start_end[t], count1 - count2);
            count1++; count2++;
            ans2 = max(ans2, count2);
        }
    }
    cout << ans1 << ' ' << ans2 << '\n';
}