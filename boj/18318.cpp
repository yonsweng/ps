#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template<typename T> class SegTree {
    // Segment tree가 구하고자 하는 값에 따라 변경
    const T BOUND = 0;
    inline T f(T a, T b) { return max(a, b); }

    struct Node {
        int s, e;
        T value;
        int l, r;
        Node(int s, int e, T value, int l, int r): s(s), e(e), value(value), l(l), r(r) {}
    };
    vector<Node> node;
    int MIN, MAX;

    T query(int k, int req_s, int req_e) {
        if(req_e < node[k].s || node[k].e < req_s)
            return BOUND;
        if(req_s <= node[k].s && node[k].e <= req_e)
            return node[k].value;
        T left = node[k].l != -1 ? query(node[k].l, req_s, req_e) : BOUND;
        T right = node[k].r != -1 ? query(node[k].r, req_s, req_e) : BOUND;
        return f(left, right);
    }
    void update(int k, int req_i, T value) {
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
        T left = node[k].l != -1 ? node[node[k].l].value : BOUND;
        T right = node[k].r != -1 ? node[node[k].r].value : BOUND;
        node[k].value = f(left, right);
    }
public:
    SegTree(int MIN, int MAX) : MIN(MIN), MAX(MAX) { node.emplace_back(MIN, MAX, BOUND, -1, -1); }
    T query(int start, int end) { return query(0, start, end); }
    void update(int i, T value) { update(0, i, value); }
};

struct PP {
    int x1, y1, x2, y2;
    PP(int x1, int y1, int x2, int y2) : x1(x1), y1(y1), x2(x2), y2(y2) {}
};

inline long long dist(PP &p) {
    return abs(p.x1 - p.x2) + abs(p.y1 - p.y2);
}

int main() {
    freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N, P;
    cin >> N >> P;

    vector<PP> p;
    vector<pair<pair<int, int>, pair<int, int>>> s;
    p.reserve(P);
    s.reserve(2 * P);
    for(int i = 0; i < P; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        p.emplace_back(x1, y1, x2, y2);
        s.emplace_back(make_pair(x1, y1), make_pair(1, i));
        s.emplace_back(make_pair(x2, y2), make_pair(-1, i));
    }

    sort(s.begin(), s.end());

    SegTree<long long> st(0, N);
    vector<long long> d(P);
    for(auto s : s) {
        if(s.second.first == -1) {
            // 도착점
            st.update(p[s.second.second].y2, d[s.second.second] + dist(p[s.second.second]));
        } else {
            // 출발점
            d[s.second.second] = max(d[s.second.second], st.query(0, p[s.second.second].y1));
        }
    }

    PP end_point(0, 0, N, N);
    cout << dist(end_point) - st.query(0, N);
}