#include <bits/stdc++.h>

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
    vector<int> v = {1, 2, 3, 4, 5, 6, 7};
    SegTree<int> st(0, 6);
    for(int i=0; i<(int)v.size(); i++) {
        st.update(i, v[i]);
    }
    cout << st.query(0, 3) << endl;
    cout << st.query(3, 6) << endl;
    cout << st.query(2, 5) << endl;
}