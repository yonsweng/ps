#include <bits/stdc++.h>

using namespace std;

inline bool is_right(long long a1, long long b1, long long a2, long long b2, int x0) {
    return b2 - b1 <= (a1 - a2) * x0;
}

inline bool is_right(long long a1, long long b1, long long a2, long long b2, long long a3, long long b3) {
    return (b2 - b1) * (a2 - a3) < (b3 - b2) * (a1 - a2);
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, int>> A(N+1);
    for(int i=1; i<=N; i++) {
        cin >> A[i].first >> A[i].second;
    }
    sort(A.begin() + 1, A.end());

    stack<int> s;
    for(int i=1; i<=N; i++) {
        if(s.empty()) {
            s.push(i);
        } else {
            while(!s.empty()) {
                if(A[s.top()].second > A[i].second) {
                    break;
                }
                s.pop();
            }
            s.push(i);
        }
    }

    N = s.size();

    vector<int> w(N+1), l(N+2);
    for(int i=N; i>=1; i--) {
        w[i] = A[s.top()].first;
        l[i] = A[s.top()].second;
        s.pop();
    }

    vector<long long> dp(N+1);
    vector<int> st;
    st.push_back(0);
    for(int i=1; i<=N; i++) {
        int j = 0;
        if(st.size() >= 2) {
            int low = 0, high = int(st.size()) - 2;
            while(low <= high) {
                int mid = (low + high) / 2;
                int k1 = st[mid], k2 = st[mid+1];

                long long a1 = l[k1+1], b1 = dp[k1];
                long long a2 = l[k2+1], b2 = dp[k2];
                if(is_right(a1, b1, a2, b2, w[i])) {
                    j = k2;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        dp[i] = dp[j] + (long long)w[i] * l[j+1];

        while(st.size() >= 2) {
            int e = int(st.size()) - 1;
            int k1 = st[e-1], k2 = st[e];
            long long a1 = l[k1+1], b1 = dp[k1];
            long long a2 = l[k2+1], b2 = dp[k2];
            long long a3 = l[i+1], b3 = dp[i];
            if(is_right(a1, b1, a2, b2, a3, b3)) {
                break;
            }
            st.pop_back();
        }
        st.push_back(i);
    }

    cout << dp[N];

    return 0;
}