#include <bits/stdc++.h>

using namespace std;

int main() {
    cin.tie(0); cout.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int i = 0; i < N; i++) {
            int t;
            cin >> t;
            pq.push(t);
        }
        long long ret = 0;
        while (pq.size() > 1) {
            int a, b;
            a = pq.top(); pq.pop();
            b = pq.top(); pq.pop();
            ret += a + b;
            pq.push(a + b);
        }
        cout << ret << '\n';
    }
}