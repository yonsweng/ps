#include <bits/stdc++.h>

using namespace std;

template<typename T> class SegTree {
    int MIN, MAX;
    vector<T> node;
    
    T f(T a, T b) { return a + b; }

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
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) { node.resize(4 * (MAX - MIN)); }
    T query(int start, int end) { return query(1, MIN, MAX, start, end); }
    void update(int i, T add) { update(1, MIN, MAX, i, add); }
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