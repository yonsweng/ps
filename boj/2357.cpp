#include <bits/stdc++.h>

using namespace std;

const int INF = 1000000000;

class SegTree {
    struct Node {
        int s, e;
        int M;
        Node *l, *r;
        Node(int s, int e) : s(s), e(e), M(-INF), l(nullptr), r(nullptr) {}
    };

    Node *root;

    void update_(Node *now, int i, int value) {
        if (now->s == now->e) {
            now->M = value;
            return;
        }
        int mid = (now->s + now->e) / 2;
        if (i <= mid) {
            if (!now->l) now->l = new Node(now->s, mid);
            update_(now->l, i, value);
        } else {
            if (!now->r) now->r = new Node(mid + 1, now->e);
            update_(now->r, i, value);
        }
        now->M = max(now->l ? now->l->M : -INF, now->r ? now->r->M : -INF);
    }

    int get_max_(Node *now, int s, int e) {
        if (!now || e < now->s || now->e < s)
            return -INF;  // out of range
        else if (s <= now->s && now->e <= e)
            return now->M;  // included
        else
            return max(get_max_(now->l, s, e), get_max_(now->r, s, e));
    }

    void delete_nodes(Node *now) {
        if (!now) return;
        delete_nodes(now->l);
        delete_nodes(now->r);
        delete now;
    }

public:
    SegTree(int s, int e) { root = new Node(s, e); }
    void update(int i, int value) { update_(root, i, value); }
    int get_max(int s, int e) { return get_max_(root, s, e); }
    ~SegTree() { delete_nodes(root); }
};

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    SegTree min_tree(1, N), max_tree(1, N);
    for(int i=1; i<=N; i++) {
        int k;
        cin >> k;
        min_tree.update(i, -k);
        max_tree.update(i, k);
    }
    for(int i=1; i<=M; i++) {
        int a, b;
        cin >> a >> b;
        cout << -min_tree.get_max(a, b) << ' ' << max_tree.get_max(a, b) << '\n';
    }
}