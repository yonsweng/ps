#include <bits/stdc++.h>

#define MAXN 100000
#define MAXY 100000

using namespace std;

int N;

class PST {
    struct Node {
        int left, right;  // [left, right]
        int sum;
        Node *lchild, *rchild;

        Node(int left, int right) : left(left), right(right), sum(0), lchild(nullptr), rchild(nullptr) {}
    };

    Node *root[MAXN + 1];  // root[x]: tree of 0 ~ x-1
    vector<Node *> node_ptrs;

    Node *update_(Node *this_node, int y, bool is_new) {
        int left = this_node->left;
        int right = this_node->right;
        int mid = (left + right) / 2;

        Node *new_node;
        if (!is_new) {
            new_node = new Node(left, right);
            node_ptrs.push_back(new_node);
            new_node->lchild = this_node->lchild;
            new_node->rchild = this_node->rchild;
        } else
            new_node = this_node;

        // Leaf node
        if (left == right) {
            new_node->sum = this_node->sum + 1;
            return new_node;
        }

        if (y <= mid) {  // Left
            if (!new_node->lchild) {
                new_node->lchild = new Node(left, mid);
                node_ptrs.push_back(new_node->lchild);
                update_(new_node->lchild, y, true);
            } else
                new_node->lchild = update_(new_node->lchild, y, false);
        } else {  // Right
            if (!new_node->rchild) {
                new_node->rchild = new Node(mid + 1, right);
                node_ptrs.push_back(new_node->rchild);
                update_(new_node->rchild, y, true);
            } else
                new_node->rchild = update_(new_node->rchild, y, false);
        }

        int sum = 0;
        if (new_node->lchild) sum += new_node->lchild->sum;
        if (new_node->rchild) sum += new_node->rchild->sum;
        new_node->sum = sum;
        return new_node;
    }

    int get_sum_(Node *here, int b, int t) {
        if (!here || t < here->left || here->right < b)
            return 0;
        else if (b <= here->left && here->right <= t)
            return here->sum;
        else
            return get_sum_(here->lchild, b, t) + get_sum_(here->rchild, b, t);
    }

public:
    PST() {
        root[0] = new Node(0, N);
        node_ptrs.push_back(root[0]);
        for (int i = 1; i <= N; i++) root[i] = nullptr;
    }

    void update(int xi, int y) {
        if (!root[xi + 1])
            root[xi + 1] = update_(root[xi], y, false);
        else
            update_(root[xi + 1], y, true);
    }

    // Sum of 0 ~ x-1
    int get_sum(int xi, int b, int t) {
        return get_sum_(root[xi + 1], b, t);
    }

    ~PST() {
        for (Node *p : node_ptrs) delete p;
    }
};

vector<int> idx[MAXN + 1];

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    cin >> N;

    vector<int> A(N + 1);
    for(int i=1; i<=N; i++) {
        cin >> A[i];
        idx[A[i]].push_back(i);
    }

    PST pst;

    for(int j=0; j<N; j++) {
        if(idx[j].empty()) {
            pst.update(j, 0);
        }
        for(int k : idx[j])
            pst.update(j, k);
    }

    long long sum = 0;
    cout << 0 << '\n';
    for(int j=1; j<N; j++) {
        for(int k : idx[j-1]) {
            sum += (k - 1) - pst.get_sum(j-1, 1, k-1);
        }
        cout << sum << '\n';
    }
}