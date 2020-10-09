#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct MergeSortTree {
    struct Node {
        int s, e;
        vector<int> d;
        Node *l, *r;
        Node(int s, int e): s(s), e(e) {}
    };

    Node *root;

    MergeSortTree(int s, int e, vector<int> &d) {
        root = new Node(s, e);
        init(d, root);
    }

    void init(vector<int> &d, Node *now) {
        if(now->s == now->e) {
            now->d.push_back(d[now->s]);
            return;
        }

        int m = (now->s + now->e) / 2;
        now->l = new Node(now->s, m), now->r = new Node(m+1, now->e);
        init(d, now->l), init(d, now->r);

        // Merge
        vector<int> &ld = now->l->d, &rd = now->r->d, &nd = now->d;
        int li = 0, ri = 0, ln = ld.size(), rn = rd.size();
        while(li < ln || ri < rn) {
            if(ri == rn) nd.push_back(ld[li++]);
            else if(li == ln) nd.push_back(rd[ri++]);
            else if(ld[li] < rd[ri]) nd.push_back(ld[li++]);
            else nd.push_back(rd[ri++]);
        }
    }

    // Return the number of elements larger than k in [i, j].
    int n_larger_than(int i, int j, int k, Node *now) {
        if(now->e < i || j < now->s)
            return 0;
        if(i <= now->s && now->e <= j)
            return now->d.end() - upper_bound(now->d.begin(), now->d.end(), k);
        else
            return n_larger_than(i, j, k, now->l) + n_larger_than(i, j, k, now->r);
    }
};

struct Card {
    int a, l, r;
    bool operator<(const Card &c) {
        return a < c.a;
    }
};

int main() {
    freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n;
    vector<Card> c;
    vector<int> d;

    cin >> n;
    c.resize(n+1);
    d.resize(n+1);
    for(int i=1; i<=n; i++) {
        cin >> c[i].a;
        d[i] = c[i].a;
    }

    MergeSortTree mst(1, n, d);

    for(int i=1; i<=n; i++) {
        c[i].l = mst.n_larger_than(1, i-1, c[i].a, mst.root);
        c[i].r = mst.n_larger_than(i+1, n, c[i].a, mst.root);
    }

    sort(c.begin() + 1, c.end());

    long long answer = 0;
    for(int i=1; i<=n; i++)
        answer += min(c[i].l, c[i].r);
    cout << answer;
}