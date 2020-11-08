#include <iostream>
#include <vector>
#include <string>
#include <cmath>

#define INF 987654321

using namespace std;

template<typename T> class SegTree {
    // Segment tree가 구하고자 하는 값에 따라 변경
    const T BOUNDARY = INF;
    T f(T a, T b) { return min(a, b); }

    int MIN, MAX;
    vector<T> node;

    T query(int node_num, int node_s, int node_e, int req_s, int req_e) {
        if (req_e < node_s || node_e < req_s)
            return BOUNDARY;
        if (req_s <= node_s && node_e <= req_e)
            return node[node_num];
        int node_m = (node_s + node_e) / 2;
        T left = query(node_num * 2, node_s, node_m, req_s, req_e);
        T right = query(node_num * 2 + 1, node_m + 1, node_e, req_s, req_e);
        return f(left, right);
    }
    void update(int node_num, int node_s, int node_e, int req_i, T value) {
        if (req_i < node_s || node_e < req_i)
            return;
        if (node_s == node_e) {
            node[node_num] = value;
            return;
        }
        int node_m = (node_s + node_e) / 2;
        update(node_num * 2, node_s, node_m, req_i, value);
        update(node_num * 2 + 1, node_m + 1, node_e, req_i, value);
        node[node_num] = f(node[node_num * 2], node[node_num * 2 + 1]);
    }
public:
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) {
        node.resize(4 * (MAX - MIN));
        fill(node.begin(), node.end(), BOUNDARY);
    }
    T query(int start, int end) { return query(1, MIN, MAX, start, end); }
    void update(int i, T add) { update(1, MIN, MAX, i, add); }
};

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    string s, t;
    s.resize(n+1), t.resize(n+1);
    for(int i=1; i<=n; i++) cin >> s[i];
    for(int i=1; i<=n; i++) cin >> t[i];

    vector<int> dp(n+1), b(n+1);
    SegTree<int> st(0, n-1);

    dp[0] = 0;
    b[0] = b[1] = 0;

    for(int i=2; i<=n; i++) {
        if(t[i-1] != t[i])
            b[i] = b[i-1] + 1;
        else
            b[i] = b[i-1];
    }

    for(int i=1; i<=n; i++) {
        st.update(i-1, 2 * dp[i-1] - b[i]);
        // cout << st.query(i-k, i-1) << '\n';

        if(s[i] == t[i])
            dp[i] = dp[i-1];
        else
            dp[i] = int(ceil((st.query(max(i-k, 0), i-1) + b[i] + 2) / 2.0));
    }

    cout << dp[n];

    return 0;
}