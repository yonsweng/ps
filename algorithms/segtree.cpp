class SegTree {
    struct Node {
        int b, e;
        long long s;
        Node *l, *r;

        Node(int b, int e) : b(b), e(e), s(0), l(nullptr), r(nullptr) {}
    };

    Node *root;

    void update_(Node *now, int i, int value) {
        if (now->b == now->e) {
            now->s = value;
            return;
        }

        int mid = (now->b + now->e) / 2;
        if (i <= mid) {
            if (!now->l) now->l = new Node(now->b, mid);
            update_(now->l, i, value);
        } else {
            if (!now->r) now->r = new Node(mid + 1, now->e);
            update_(now->r, i, value);
        }

        long long sum = 0;
        if (now->l) sum += now->l->s;
        if (now->r) sum += now->r->s;
        now->s = sum;
    }

    long long get_sum_(Node *now, int b, int e) {
        if (!now || e < now->b || now->e < b)
            return 0;  // out of range
        else if (b <= now->b && now->e <= e)
            return now->s;  // included
        else
            return get_sum_(now->l, b, e) + get_sum_(now->r, b, e);
    }

    void delete_nodes(Node *now) {
        if (!now) return;
        delete_nodes(now->l);
        delete_nodes(now->r);
        delete now;
    }

public:
    SegTree(int N) {
        root = new Node(1, N);
    }

    void update(int i, int value) {
        update_(root, i, value);
    }

    long long get_sum(int b, int e) {
        return get_sum_(root, b, e);
    }

    ~SegTree() {
        delete_nodes(root);
    }
};