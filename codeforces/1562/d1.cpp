#include <iostream>
#include <vector>

using namespace std;

template<typename T> class SegTree {
    // Segment tree가 구하고자 하는 값에 따라 변경
    const T BOUND = 0;
    T f(T a, T b) { return a + b; }

    int MIN, MAX;
    vector<T> node;

    T query(int k, int node_s, int node_e, int req_s, int req_e) {
        if (req_e < node_s || node_e < req_s)
            return BOUND;
        if (req_s <= node_s && node_e <= req_e)
            return node[k];
        int node_m = (node_s + node_e) / 2;
        T left = query(k * 2, node_s, node_m, req_s, req_e);
        T right = query(k * 2 + 1, node_m + 1, node_e, req_s, req_e);
        return f(left, right);
    }
    void update(int k, int node_s, int node_e, int req_i, T value) {
        if (req_i < node_s || node_e < req_i)
            return;
        if (node_s == node_e) {
            node[k] = value;
            return;
        }
        int node_m = (node_s + node_e) / 2;
        update(k * 2, node_s, node_m, req_i, value);
        update(k * 2 + 1, node_m + 1, node_e, req_i, value);
        node[k] = f(node[k * 2], node[k * 2 + 1]);
    }
public:
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) { node.resize(4 * (MAX - MIN)); }
    T query(int start, int end) { return query(1, MIN, MAX, start, end); }
    void update(int i, T value) { update(1, MIN, MAX, i, value); }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    int t;
    cin >> t;

    for(int i=0; i<t; i++) {
        int n, q;
        cin >> n >> q;

        string ss;
        cin >> ss;

        SegTree<int> st(0, n);

        for(int j=0; j<n; j++) {
            int sign = j % 2 == 0 ? 1 : -1;
            if(ss[j] == '-')
                sign *= -1;
            st.update(j, sign > 0 ? 1 : 0);
        }

        // cout << "sum: " << st.query(0, n-1) << '\n';

        for(int j=0; j<q; j++) {
            int l, r;
            cin >> l >> r;

            int num_pos = st.query(l-1, r-1);
            int num_neg = r-l+1 - num_pos;

            int diff = abs(num_pos - num_neg);

            if(diff == 0)
                cout << "0\n";
            else if(diff % 2 == 1)
                cout << "1\n";
            else
                cout << "2\n";
        }
    }
}