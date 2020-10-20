#include <bits/stdc++.h>

using namespace std;

template<typename T> class SegTree {
    int size;
    vector<T> node;

    T f(T a, T b) {
        return max(a, b);
    }

    T query(int node_num, int node_s, int node_e, int req_s, int req_e) {
        if (node_s > req_e || node_e < req_s)
            return 0;
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
        if(node_s == node_e) {
            node[node_num] = value;
            return;
        }
        int node_m = (node_s + node_e) / 2;
        update(node_num * 2, node_s, node_m, req_i, value);
        update(node_num * 2 + 1, node_m + 1, node_e, req_i, value);
        node[node_num] = f(node[node_num * 2], node[node_num * 2 + 1]);
    }

public:
    SegTree(int n) {
        size = n;
        node.resize(4 * size);
    }

    T query(int start, int end) {
        return query(1, 0, size - 1, start, end);
    }

    void update(int i, T add) {
        update(1, 0, size - 1, i, add);
    }
};

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> Q(n+1), a(n+1, 1), b(n+1, 1), c(n+1), d(n+1);
    SegTree<int> ta(n), tb(n), tc(n), td(n);

    for(int i=1; i<=n; i++)
        cin >> Q[i];

    // coordinate compression
    vector<int> s;
    for(int i=1; i<=n; i++) s.push_back(Q[i]);
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());
    for(int i=1; i<=n; i++)
        Q[i] = lower_bound(s.begin(), s.end(), Q[i]) - s.begin();

    // a[i]: ~ seq[i-1]은 UD-seq이고 seq[i-1] < seq[i]인 부분수열 중 가장 긴 것의 길이.
    // b[i]: ~ seq[i-1]은 UD-seq이고 seq[i-1] > seq[i]인 부분수열 중 가장 긴 것의 길이.
    // c[i]: Q[i]를 포함하고 마지막에 증가하는 UD-seq 중 가장 긴 것의 길이.
    // d[i]: Q[i]를 포함하고 마지막에 감소하는 UD-seq 중 가장 긴 것의 길이.
    // ta.query(m, M): m <= Q[i] <= M인 a[i]의 최댓값.
    for(int i=2; i<=n; i++) {
        ta.update(Q[i-1], a[i-1]);
        tb.update(Q[i-1], b[i-1]);
        tc.update(Q[i-1], c[i-1]);
        td.update(Q[i-1], d[i-1]);
        a[i] = max(ta.query(0, Q[i]-1), max(tc.query(0, Q[i]-1), td.query(0, Q[i]-1))) + 1;
        b[i] = max(tb.query(Q[i]+1, n-1), max(tc.query(Q[i]+1, n-1), td.query(Q[i]+1, n-1))) + 1;
        int taq = ta.query(0, Q[i]-1);
        int tbq = tb.query(Q[i]+1, n-1);
        c[i] = taq >= 2 ? taq + 1 : 0;
        d[i] = tbq >= 2 ? tbq + 1 : 0;
    }

    int m = 0;
    for(int i=1; i<=n; i++) {
        m = max(m, c[i]);
        m = max(m, d[i]);
    }

    // for(int i=1; i<=n; i++) cout << a[i] << ' '; cout << '\n';
    // for(int i=1; i<=n; i++) cout << b[i] << ' '; cout << '\n';
    // for(int i=1; i<=n; i++) cout << c[i] << ' '; cout << '\n';
    // for(int i=1; i<=n; i++) cout << d[i] << ' '; cout << '\n';

    cout << m;
}