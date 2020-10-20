#include <bits/stdc++.h>

using namespace std;

template<typename T> class SegTree {
    int MIN, MAX;
    vector<T> node, lazy;

    T init(int node_num, int node_s, int node_e, const vector<T>& data) {
        if (node_s == node_e)
            return node[node_num] = data[node_s];
        int node_m = (node_s + node_e) / 2;
        T left = init(node_num * 2, node_s, node_m, data);
        T right = init(node_num * 2 + 1, node_m + 1, node_e, data);
        return node[node_num] = left + right;
    }
    void prop(int node_num, int node_s, int node_e) {
        node[node_num] += lazy[node_num] * (node_e - node_s + 1);
        if (node_s != node_e) {
            lazy[node_num * 2] += lazy[node_num];
            lazy[node_num * 2 + 1] += lazy[node_num];
        }
        lazy[node_num] = 0;
    }
    T query(int node_num, int node_s, int node_e, int req_s, int req_e) {
        prop(node_num, node_s, node_e);
        if (node_s > req_e || node_e < req_s)
            return 0;
        if (req_s <= node_s && node_e <= req_e)
            return node[node_num];
        int node_m = (node_s + node_e) / 2;
        T left = query(node_num * 2, node_s, node_m, req_s, req_e);
        T right = query(node_num * 2 + 1, node_m + 1, node_e, req_s, req_e);
        return left + right;
    }
    void update(int node_num, int node_s, int node_e, int req_s, int req_e, T value) {
        prop(node_num, node_s, node_e);
        if (req_e < node_s || node_e < req_s)
            return;
        if (req_s <= node_s && node_e <= req_e) {
            lazy[node_num] += value;
            prop(node_num, node_s, node_e);
            return;
        }
        int node_m = (node_s + node_e) / 2;
        update(node_num * 2, node_s, node_m, req_s, req_e, value);
        update(node_num * 2 + 1, node_m + 1, node_e, req_s, req_e, value);
        node[node_num] = node[node_num * 2] + node[node_num * 2 + 1];
    }
public:
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) {
        node.resize(4 * (MAX - MIN));
        lazy.resize(4 * (MAX - MIN));
    }
    SegTree(const vector<T>& data) : MIN(0), MAX(int(data.size())) {
        node.resize(4 * (MAX - MIN));
        lazy.resize(4 * (MAX - MIN));
        init(1, MIN, MAX, data);
    }
    T query(int start, int end) { return query(1, MIN, MAX, start, end); }
    void update(int start, int end, T value) { update(1, MIN, MAX, start, end, value); }
};

int main() {
    vector<int> v = {1, 2, 3, 4, 6};
    SegTree<int> st(v);
    cout << st.query(1, 4) << endl;
    st.update(2, 3, 1);
    cout << st.query(1, 4) << endl;
}