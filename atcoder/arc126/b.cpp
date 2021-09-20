#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

template<typename T> class SegTree {
    int MIN, MAX;
    vector<T> node;

    T f(T a, T b) { return max(a, b); }

    T query(int node_num, int node_s, int node_e, int req_s, int req_e) {
        if (req_e < node_s || node_e < req_s)
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
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) { node.resize(4 * (MAX - MIN)); }
    T query(int start, int end) { return query(1, MIN, MAX, start, end); }
    void update(int i, T add) { update(1, MIN, MAX, i, add); }
};


int main() {
    ios::sync_with_stdio(false), cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<pair<int, int> > a;
    for(int i=0; i<M; i++) {
        int ai, bi;
        cin >> ai >> bi;
        a.emplace_back(ai, bi);
    }
    sort(a.begin(), a.end());

    SegTree<int> st(0, N+1);
    int pre = 0;
    stack<pair<int, int> > tmp;
    for(auto t : a) {
        if(t.first != pre)
            while(!tmp.empty()) {
                auto top = tmp.top();
                tmp.pop();
                st.update(top.first, top.second);
            }
        pre = t.first;
        int max_val = st.query(1, t.second - 1);
        tmp.push(make_pair(t.second, max_val + 1));
    }
    while(!tmp.empty()) {
        auto top = tmp.top();
        tmp.pop();
        st.update(top.first, top.second);
    }
    cout << st.query(1, N);
    // for t in a:
    //     if t[0] != pre:
    //         for tmp_ in tmp:
    //             st.update(tmp_[0], tmp_[1])
    //     max_ = st.query(1, t[1]-1)
    //     tmp.append((t[1], max_ + 1))
    //     pre = t[0]
    // for tmp_ in tmp:
    //     st.update(tmp_[0], tmp_[1])
    // print(st.query(1, N))
}