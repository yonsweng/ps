#include <bits/stdc++.h>

using namespace std;

template<typename T> class SegTree {
    // Segment tree가 구하고자 하는 값에 따라 변경
    const pair<T, int> BOUND = {0, -1};
    inline pair<T, int> f(pair<T, int> a, pair<T, int> b) {
        if(a.first >= b.first)
            return a;
        else
            return b;
    }

    struct Node {
        int s, e;
        pair<T, int> value;
        int l, r;
        Node(int s, int e, pair<T, int> value, int l, int r): s(s), e(e), value(value), l(l), r(r) {}
    };
    vector<Node> node;
    int MIN, MAX;

    pair<T, int> query(int k, int req_s, int req_e) {
        if(req_e < node[k].s || node[k].e < req_s)
            return BOUND;
        if(req_s <= node[k].s && node[k].e <= req_e)
            return node[k].value;
        auto left = node[k].l != -1 ? query(node[k].l, req_s, req_e) : BOUND;
        auto right = node[k].r != -1 ? query(node[k].r, req_s, req_e) : BOUND;
        return f(left, right);
    }
    void update(int k, int req_i, pair<T, int> value) {
        if (node[k].s == node[k].e) {
            node[k].value = f(node[k].value, value);
            return;
        }
        int m = (node[k].s + node[k].e) / 2;
        if(req_i <= m) {
            if(node[k].l == -1) {
                node[k].l = node.size();
                node.emplace_back(node[k].s, m, BOUND, -1, -1);
            }
            update(node[k].l, req_i, value);
        } else {
            if(node[k].r == -1) {
                node[k].r = node.size();
                node.emplace_back(m + 1, node[k].e, BOUND, -1, -1);
            }
            update(node[k].r, req_i, value);
        }
        auto left = node[k].l != -1 ? node[node[k].l].value : BOUND;
        auto right = node[k].r != -1 ? node[node[k].r].value : BOUND;
        node[k].value = f(left, right);
    }
public:
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) { node.emplace_back(MIN, MAX, BOUND, -1, -1); }
    pair<T, int> query(int start, int end) { return query(0, start, end); }
    void update(int i, pair<T, int> value) { update(0, i, value); }
};

bool comp(const pair<int, int> a, const pair<int, int> b) {
    return a.first < b.first || (a.first == b.first && a.second > b.second);
}

int max_idx(int dp[], int N) {
    int mi = 0;
    for(int i=1; i<N; i++) {
        if(dp[i] > dp[mi])
            mi = i;
    }
    return mi;
}

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    SegTree<int> st(1, 1000000);
    int N;
    cin >> N;
    pair<int, int> seg[100000];
    for(int i=0; i<N; i++) {
        cin >> seg[i].first >> seg[i].second;
    }

    sort(seg, seg+N, comp);
    // first 오름차순 -> second 내림차순

    int dp[100000];
    int prev[100000];
    prev[0] = -1, dp[0] = 1;
    for(int i=1; i<N; i++) {
        st.update(seg[i-1].second, make_pair(dp[i-1], i-1));
        auto q = st.query(seg[i].second, 1000000);
        dp[i] = q.first + 1, prev[i] = q.second;
    }

    stack<pair<int, int>> s;
    for(int i=max_idx(dp, N); i!=-1; i=prev[i]) {
        s.push(seg[i]);
    }

    cout << s.size();
    while(!s.empty()) {
        cout << '\n' << s.top().first << ' ' << s.top().second;
        s.pop();
    }

    return 0;
}