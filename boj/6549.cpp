#include <bits/stdc++.h>

using namespace std;

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    // while(true) {
        int n;
        cin >> n;

        // if(n == 0)
        //     break;

        int h[100002];
        h[0] = -1;
        for(int i = 1; i <= n; i++)
            cin >> h[i];
        h[n + 1] = 0;

        long long answer = 0;
        stack<int> s;
        s.push(0);
        s.push(1);
        for(int i = 2; i <= n + 1; i++) {
            while(true) {
                if(h[i] > h[s.top()])
                    break;
                int j = s.top();
                s.pop();
                int width = i - s.top() - 1;
                long long area = (long long)width * h[j];
                answer = max(answer, area);
            }
            s.push(i);
        }

        cout << answer << '\n';
    // }
}