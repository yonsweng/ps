#include <bits/stdc++.h>

using namespace std;

template<typename T> class SegTree {
    int MIN, MAX;
    vector<T> node, lazy;

    T init(int k, int node_s, int node_e, const vector<T>& data) {
        if (node_s == node_e)
            return node[k] = data[node_s];
        int node_m = (node_s + node_e) / 2;
        T left = init(k * 2, node_s, node_m, data);
        T right = init(k * 2 + 1, node_m + 1, node_e, data);
        return node[k] = left + right;
    }
    void prop(int k, int node_s, int node_e) {
        node[k] += lazy[k] * (node_e - node_s + 1);
        if (node_s != node_e) {
            lazy[k * 2] += lazy[k];
            lazy[k * 2 + 1] += lazy[k];
        }
        lazy[k] = 0;
    }
    T query(int k, int node_s, int node_e, int req_s, int req_e) {
        prop(k, node_s, node_e);
        if (req_e < node_s || node_e < req_s)
            return 0;
        if (req_s <= node_s && node_e <= req_e)
            return node[k];
        int node_m = (node_s + node_e) / 2;
        T left = query(k * 2, node_s, node_m, req_s, req_e);
        T right = query(k * 2 + 1, node_m + 1, node_e, req_s, req_e);
        return left + right;
    }
    void update(int k, int node_s, int node_e, int req_s, int req_e, T add) {
        prop(k, node_s, node_e);
        if (req_e < node_s || node_e < req_s)
            return;
        if (req_s <= node_s && node_e <= req_e) {
            lazy[k] += add;
            prop(k, node_s, node_e);
            return;
        }
        int node_m = (node_s + node_e) / 2;
        update(k * 2, node_s, node_m, req_s, req_e, add);
        update(k * 2 + 1, node_m + 1, node_e, req_s, req_e, add);
        node[k] = node[k * 2] + node[k * 2 + 1];
    }
public:
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) {
        node.resize(4 * (MAX - MIN));
        lazy.resize(4 * (MAX - MIN));
    }
    SegTree(const vector<T>& data) : MIN(0), MAX(int(data.size()) - 1) {
        node.resize(4 * (MAX - MIN));
        lazy.resize(4 * (MAX - MIN));
        init(1, MIN, MAX, data);
    }
    T query(int start, int end) { return query(1, MIN, MAX, start, end); }
    void update(int start, int end, T add) { update(1, MIN, MAX, start, end, add); }
};

int main() {
	ios::sync_with_stdio(false), cin.tie(nullptr);
	int N, M, K;
	cin >> N >> M >> K;
	vector<long long> data(N);
	for(int i=0; i<N; i++)
		cin >> data[i];
	SegTree<long long> st(data);
	for(int i=0; i<M+K; i++) {
		int cmd;
		cin >> cmd;
		if(cmd == 1) {
			int b, c; long long d;
			cin >> b >> c >> d;
			st.update(b-1, c-1, d);
		} else {
			int b, c;
			cin >> b >> c;
			cout << st.query(b-1, c-1) << '\n';
		}
	}
}